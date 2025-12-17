import cv2
import torch
import time
import os

from notifier import send_email_notification, send_push_notification
from geo import get_location_and_time

print("[SYSTEM] Loading YOLO model...")
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
print("[SYSTEM] Model loaded")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Camera not accessible")
    exit()

recording = False
video_writer = None
start_time = None
video_file = "alert.avi"

print("[SYSTEM] Running — press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results.pandas().xyxy[0]

    if len(detections) > 0:
        for _, row in detections.iterrows():
            if row["confidence"] < 0.5:
                continue

            label = row["name"]

            if label == "person":
                message = "A person has been captured."
            elif label == "cow":
                message = "A cow has been captured in your yard."
            else:
                message = "Moving object captured in your yard."

            info = f"{message}\n\n{get_location_and_time()}"

            if not recording:
                recording = True
                start_time = time.time()

                snapshot = "alert.jpg"
                cv2.imwrite(snapshot, frame)

                send_email_notification("🚨 Security Alert", info, snapshot)
                send_push_notification(message)

                fourcc = cv2.VideoWriter_fourcc(*"XVID")
                video_writer = cv2.VideoWriter(
                    video_file, fourcc, 20.0,
                    (frame.shape[1], frame.shape[0])
                )

            video_writer.write(frame)

            if time.time() - start_time >= 5:
                recording = False
                video_writer.release()
                send_email_notification("🚨 Security Video Alert", info, video_file)
                send_push_notification(message + " (video)")
                video_writer = None

    else:
        if recording:
            recording = False
            if video_writer:
                video_writer.release()
            if os.path.exists(video_file):
                os.remove(video_file)

    cv2.imshow("Home Security", frame)
    if cv2.waitKey(1) & 0xFF in [ord("q"), ord("Q")]:
        break

cap.release()
cv2.destroyAllWindows()
