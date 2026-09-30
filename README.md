# Supermarket Product Detection using YOLO

## Project Overview

This project develops a computer vision system for detecting supermarket products in images using YOLO object detection.

The system identifies products, draws bounding boxes around them, and displays confidence scores for each detection.

## Problem Description

Supermarkets contain many products displayed on shelves. Manually identifying products from images can be time-consuming.

The goal of this project is to automatically detect and classify supermarket products from images.

## Expected Output

The system can:

- Detect supermarket products
- Identify the product class
- Draw bounding boxes
- Display confidence scores

## Dataset & Model Used

The project uses supermarket product images from public datasets such as Roboflow and Kaggle.

A pretrained and fine-tuned YOLO model was used for object detection.

The model supports many supermarket-related classes such as:

- Apple
- Banana
- Avocado
- Coffee
- Cheese
- Milk
- Meat
- Yogurt
- Bread
- Tomato
- Cucumber
- Juice
- Eggs

## Workflow / Architecture

Input Image  
↓  
Image Preprocessing  
↓  
YOLO Object Detection Model  
↓  
Product Detection  
↓  
Product Classification  
↓  
Bounding Boxes + Confidence Scores  
↓  
Final Output Image

## Results & Evaluation

The model was tested on four supermarket images.

### Test Image 1
The model detected:

- 59 Beans

### Test Image 2
The model detected:

- 5 Avocados
- 4 Nectarines
- 3 Plums
- 2 Apples

### Test Image 3
The model detected:

- 21 Cheeses
- 3 Meats
- 1 Yogurt

### Test Image 4
The model detected:

- 33 Coffee products

## Successful Prediction

The coffee shelf image is a successful prediction example.

The model detected many coffee products correctly and classified them as Coffee.

## Failure Case

The fruit image shows a failure case.

Some apples were incorrectly classified as:

- Avocado
- Nectarine
- Plum

This may happen because these fruits have similar colors, shapes, and visual features.

Another failure occurred in a crowded shelf image where many products were classified as Beans.

## Deployment / Optimization

The YOLO model was exported to ONNX format.

The ONNX file can be used for deployment on different platforms and applications.

Possible applications include:

- Inventory monitoring
- Shelf monitoring
- Smart checkout systems
- Mobile supermarket applications
- Automatic product detection

## Technologies Used

- Python
- YOLO
- Ultralytics
- PyTorch
- OpenCV
- Roboflow
- Kaggle
- VS Code
- ONNX

## How to Run the Project

Install Ultralytics:

```bash
pip install ultralytics