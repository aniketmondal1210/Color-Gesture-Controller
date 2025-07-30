# Color-Gesture-Controller 🎥🖐️

Control your keyboard using hand gestures detected via webcam! This project tracks yellow-colored objects in real-time and simulates a spacebar press when upward motion is detected. 🚀 Perfect for touchless interaction and basic gesture automation. 💡⌨️

---

## 🔧 Features

- Tracks yellow objects using OpenCV 🎨
- Detects upward movement 🆙
- Simulates a spacebar press with `pyautogui` ⌨️
- Real-time webcam feed with object detection 📷

---

## 📦 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- PyAutoGUI

Install dependencies:

```bash
pip install opencv-python numpy pyautogui
```

🚀 How It Works

    Webcam feed is accessed using OpenCV.

    The image is converted to HSV to isolate yellow colors.

    If a yellow object moves upward (based on Y-coordinate), pyautogui triggers a spacebar press.

    A bounding box is drawn around detected yellow objects.

▶️ Usage

Run the script:

```bash
python color_gesture_controller.py
```

Exit by pressing q.

💡 Use Cases

    Gesture-based game control 🕹️

    Touchless slide changers 🖼️

    Basic automation interfaces 🤖

    Fun computer interaction project 😄

📸 Demo

Coming soon! 📷🎬

📄 License

This project is licensed under the MIT License.
