
# AI Enabled Home Security System

An AI-powered home security system built with Python that uses computer vision to monitor activity through a camera feed and send alerts when suspicious behavior is detected which are movements around your premises mostly.

This project is designed as a **learning-focused, practical implementation** of AI, computer vision, and automation for real‑world security use cases.

---

## 🚀 Features

* 📷 **Real-time camera monitoring**
* 🧠 **AI-based detection** (motion / object / human detection)
* 🌍 **Geolocation support** for contextual alerts (this was just added for fun since the owner of the system knows the location  already)
* 🔔 **Automated notifications** when a threat is detected
* ⚙️ **Configurable system settings**
* 🐍 Built entirely with **Python**

---

## 🗂 Project Structure

```
AI_enabled_home_security/
│
├── camera.py        # Handles camera input and video stream
├── config.py        # Central configuration file
├── geo.py           # Geolocation and location-based logic
├── notifier.py      # Alert and notification handling
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## 🧠 How It Works

1. The system captures live video from a connected camera.
2. Frames are processed using computer vision techniques.
3. When predefined conditions are met (e.g. motion or object detected), the system:

   * Analyzes the event
   * Attaches contextual data (time, location)
   * Sends a notification in png form to the user

This modular design allows each component to be extended or replaced easily.

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/livingemoji/AI_enabled_home_security.git
cd AI_enabled_home_security
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main camera module:

```bash
python camera.py
```

Make sure your camera device is properly connected and accessible by OpenCV and also you have to already configured you smtp password for the sender email.

---

## ⚙️ Configuration

Edit `config.py` to adjust:

* Camera index
* Detection thresholds
* Notification preferences
* Location parameters

---

## 📦 Requirements

* Python 3.8+
* OpenCV
* NumPy
* Other dependencies listed in `requirements.txt`

---

## 🔒 Use Case Examples

* Home surveillance
* Small office monitoring
* IoT security experiments
* AI & computer vision learning projects

---

## 📈 Future Improvements

* Face recognition
* Cloud-based alert dashboard
* Mobile app integration
* Yolo/ deep learning models
* Edge device optimization (Raspberry Pi)

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👤 Author

**Alex Wafula**
AI | Computer Vision | Data Science | Software Engineering

GitHub: [https://github.com/livingemoji](https://github.com/livingemoji)

---

⭐ If you find this project useful, consider giving it a star!
