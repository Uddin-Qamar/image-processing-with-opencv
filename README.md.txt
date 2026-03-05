# OpenCV Practice (Python)

A collection of  **computer vision exercises using OpenCV (cv2) in Python**.  
Each exercise is self-contained and includes:
- a Python script (`.py`)
- input image(s)
- output/result image(s)

The goal is to practice core image-processing concepts such as:
- reading/writing images
- resizing and interpolation
- drawing primitives (line, rectangle, circle, polygon, text)
- Mathematical Morphology (Erosion. Dilation, Opening, amd closing)
- basic transformations
- filtering and edge detection (more coming)

---

## Repository Structure

Each exercise lives in its own folder:
 image-processing-with-opencv/
1├── drawing_shapes/
│ ├── drawing_shapes.py
│ ├── input/
│ │ └── inputImg.jpg
│ └── output/
│   └── result.jpg
2├── morophology_operation
│ ├── erosion_dilation_morphology.py
│ ├── opening_closing_morphology.py
│ ├── input image/
│ │    └── blobs_in_circular_arrangement
│ │    └── broken-text
│ │    └── wirebond-mask
│ └── output image/
│    └── Broken_text_and_wired_image
│    └── wirebond-mask_no-wires
│    └── blobs_result
└── README.md

Note: Next all exercise will follow the same pattern.
---

## Requirements

- Python 3.9+ (any recent version is fine)
- OpenCV

Install dependencies:

```bash
pip install opencv-python-headless

## How to Run:
- Clone the Project and go to the .py directory like:
- cd drawing_shapes
- run the command like:
- python drawing_shapes.py
Note!: Remeber to install the dependencise 
