# OpenCV Practice (Python)

A collection of small **computer vision exercises using OpenCV (cv2) in Python**.  
Each exercise is self-contained and includes:
- a Python script (`.py`)
- input image(s)
- output/result image(s)

The goal is to practice core image-processing concepts such as:
- reading/writing images
- resizing and interpolation
- drawing primitives (line, rectangle, circle, polygon, text)
- basic transformations
- filtering and edge detection (more coming)

---

## Repository Structure

Each exercise lives in its own folder:
opencv-practice/
├── drawing_shapes/
│ ├── drawing_shapes.py
│ ├── input/
│ │ └── example.jpg
│ └── output/
│ └── result.jpg
├── resize_images/
│ ├── resize.py
│ ├── input/
│ └── output/
└── README.md


---

## Requirements

- Python 3.9+ (any recent version is fine)
- OpenCV

Install dependencies:

```bash
pip install opencv-python-headless

## How to Run

cd drawing_shapes
python drawing_shapes.py