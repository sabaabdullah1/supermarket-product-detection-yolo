from ultralytics import YOLO

model = YOLO("weights.pt")

model.export(format="onnx")

print("Model exported to ONNX successfully.")