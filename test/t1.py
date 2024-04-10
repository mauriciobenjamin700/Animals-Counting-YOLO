from ultralytics import YOLO


# Build a YOLOv9c model from pretrained weight
model = YOLO('yolov9c.pt')

# Display model information (optional)
model.info(detailed=True,verbose=True)


# Run inference with the YOLOv9c model on the 'bus.jpg' image
#results = model('path/to/bus.jpg')