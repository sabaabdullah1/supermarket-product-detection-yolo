from ultralytics import YOLO

model = YOLO("weights.pt")

images = [
    "IMG-20211029-WA0021.jpg",
    "61931fff217c5cc6.jpg",
    "IMG_20220219_181958.jpg",
    "coffee250.jpg"
]

for image in images:
    results = model.predict(
        source=image,
        conf=0.25,
        save=True,
        project="results",
        name="predictions",
        exist_ok=True
    )

    print(f"\n--- {image} ---")

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[class_id]

            print(
                f"{class_name}: {confidence:.2f}"
            )

print("\nDone!")