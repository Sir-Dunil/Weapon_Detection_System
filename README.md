# 🔫 Weapon Detection System

A real-time weapon and threat detection system built with YOLOv8 and OpenCV.
Designed to identify weapons and suspicious individuals through live webcam 
or pre-recorded video footage.

---

## 📸 Demo
> Demo video coming soon

---

## 📋 Overview

This system uses a custom trained YOLOv8 model to detect potential security 
threats in real time. It features a three tier threat classification system 
with color coded alerts and intelligent detection tracking to minimize 
false positives.

This project was inspired by the concept of AI powered public safety systems
and represents a practical implementation of computer vision in the 
security domain.

---

## 🎯 Detection Classes

| Class | Threat Level | Box Color | Alert |
|-------|-------------|-----------|-------|
| 🔫 Gun | HIGH THREAT | 🔴 Red | Red Banner |
| 🔪 Knife | THREAT DETECTED | 🟠 Orange | Red Banner |
| 🎭 Person with Mask | SUSPICIOUS | 🟡 Yellow | Yellow Banner |

---

## ✨ Features

- 🔴 **Real time weapon detection** via webcam or video file
- 🎯 **Three tier threat level system** — weapon, suspicious, all clear
- 🚨 **Color coded alert banners** that trigger on confirmed threats
- 📊 **Confidence score display** on each detection
- 🔁 **ByteTrack object tracking** for smoother consistent detection
- ⚡ **Detection counter threshold** to reduce flickering and false positives
- 🟢 **Live status indicator** showing current threat level

---

## 🛠️ Installation

### Prerequisites
- Python 3.13
- Webcam (for live detection)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Sir-Dunil/weapon-detection-system.git
cd weapon-detection-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your YOLO weights file:
   Place your Weapon_Detection.pt file inside a folder called YOLO_Weights/

4. Run the program:
```bash
python weapon_detection.py
```

---

## 🎮 How to Use

Launch the program
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Webcam activates automatically
System begins scanning for threats
Status Indicators:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟢 ALL CLEAR  → No threats detected
🟡 SUSPICIOUS → Masked person detected
🔴 THREAT     → Weapon detected
Press Q to quit

---

## 📊 Model Performance

### Strengths
- Consistent weapon detection in controlled environments
- Reliable masked person identification
- Effective knife detection at close to medium range
- Smooth real time performance on Apple M2

### Known Limitations
- Detection consistency depends heavily on video/camera quality
- Occasional false positives in complex environments
  (similar shaped objects at distance)
- Performance varies with lighting conditions
- Gun detection less reliable at long range

### Test Results
| Test Scenario | Gun | Knife | Mask |
|--------------|-----|-------|------|
| Personal webcam test | ✅ | ✅ | ✅ |
| CCTV footage test | ⚠️ 50-60% | ⚠️ 50-60% | ✅ |
| Low light conditions | ⚠️ | ✅ | ⚠️ |

---

## 🔧 Built With

| Technology | Purpose |
|-----------|---------|
| YOLOv8 (Ultralytics) | Object detection model |
| OpenCV | Video capture and display |
| Python 3.13 | Core programming language |
| ByteTrack | Object tracking algorithm |
| Roboflow | Dataset preparation |
| Google Colab | Model training |

---

## 🗂️ Project Structure

weapon-detection-system/
│
├── weapon_detection.py     ← Main program
├── requirements.txt        ← Dependencies
├── README.md              ← Documentation
│
├── YOLO_Weights/
│   └── Weapon_Detection.pt ← Trained model
│
└── demo/
└── demo_screenshot.png ← Demo media

---

## 🚀 Future Improvements

- [ ] Expand weapon classes (baton, taser, etc)
- [ ] Train on higher resolution CCTV datasets
- [ ] Add audio alert system
- [ ] Implement logging with timestamps
- [ ] Add multiple camera support
- [ ] Deploy on edge device (Raspberry Pi)
- [ ] Integrate with notification system

---

## ⚠️ Disclaimer

This project is developed strictly for **educational and portfolio purposes**.
It is not intended for actual deployment in security or law enforcement 
systems without proper validation, ethical review, and legal compliance.

---

## 👤 Author

**Dunil**
Computer Vision Engineer in Training
- GitHub: [@Sir-Dunil](https://github.com/Sir-Dunil)
- LinkedIn: Coming soon

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
