import torch
from ultralytics import YOLO

class YOLOv8Model:
    def __init__(self, model_path):
        # Load the model
        self.model = YOLO(model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.model.to(self.device)  # Move the model to the GPU if available

    def predict(self, frame):
        # Convert the frame to a tensor and move it to the GPU
        frame_tensor = torch.from_numpy(frame).to(self.device).float()
        # Perform inference
        results = self.model(frame_tensor)
        return results