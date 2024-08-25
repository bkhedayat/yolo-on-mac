import cv2
from detector import YOLOv8Model

# Initialize the YOLOv8 model
model = YOLOv8Model("yolov8n.pt")  # Use a sample YOLOv8 model

# Capture from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model.predict(frame)

    # Visualize the results
    for box in results.boxes:
        # Extract the coordinates and convert them to integers
        x1, y1, x2, y2 = map(int, box.xyxy[0].numpy())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Convert the class label and confidence to scalars
        class_id = int(box.cls[0].item())
        confidence = box.conf[0].item()

        # Extract the class label and confidence
        label = f"{model.model.names[class_id]} {confidence:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow("YOLOv8 Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()