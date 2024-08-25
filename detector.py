from ultralytics import YOLO

class YOLOv8Model:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
    
    def predict(self, image):
        results = self.model(image)
        return results[0]  # returning the first result for simplicity