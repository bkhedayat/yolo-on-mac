# YOLOv8 Object Detection on Mac with Apple Silicon

This repository contains a Python program for performing object detection using the YOLOv8 model on a Mac with Apple Silicon. The program captures video from the Mac's webcam, processes each frame using YOLOv8, and displays the detected objects in real-time.

## Features
- **Real-time object detection**: Leverages the YOLOv8 model for fast and accurate detection.
- **Apple Silicon support**: Designed to run efficiently on Mac computers with Apple Silicon (M1, M2, etc.).
- **CPU-only execution**: The program runs on the CPU, making it compatible with Mac's integrated hardware.

## Prerequisites

Before running the program, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package installer)

### Required Python Packages

Install the required Python packages using `pip`:

```bash
pip install ultralytics opencv-python torch
```
## Installation

### 1.  Clone the repository:
    git clone https://github.com/bkhedayat/yolov8-mac-apple-silicon.git
    cd yolov8-mac-apple-silicon

###	2.	Download the YOLOv8 model:
The program uses the YOLOv8n model, which can be downloaded automatically by the script. Ensure your internet connection is active during the first run.

## Usage
 To run the object detection program, execute the following command:

 ``` 
 python main.py
  ```