# 🧥 Invisible Cloak using OpenCV (Black Cloak Edition)

This project recreates the "invisibility cloak" effect inspired by Harry Potter using OpenCV and Python. By detecting a black-colored cloak and replacing it with the background, it makes the wearer appear invisible in real-time.

---

## 📁 Project Structure
Invisible-Cloak/
├── background.py # Captures background video (e.g., empty room)
├── invisible_cloak.py # Main script for invisibility effect
├── background.mp4 # Saved background video
├── image.jpg # Optional single frame image
├── README.md # Project documentation

---

## 🎯 Features

- Real-time video processing with OpenCV
- Detects **black color cloak** using HSV color filtering
- Replaces cloak region with background to create invisibility effect
- Saves the background as a `.mp4` file
- Works with any webcam

---

## 🛠️ Requirements

- Python 3.x
- OpenCV

### Install dependencies

```bash
pip install opencv-python numpy

## Reference Links
- https://youtu.be/EGMHG0bv-CE
- https://learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/

