# Supermarket Product Detection using YOLO

## Project Overview

This project develops a computer vision system for detecting supermarket products in images using YOLO object detection.

The system identifies supermarket products, draws bounding boxes around detected objects, and displays confidence scores for each prediction.

---

## Problem Description

Supermarkets contain many products displayed on shelves. Manually identifying and monitoring products from images can be time-consuming.

The goal of this project is to develop a computer vision system that can automatically detect and classify supermarket products from images.

---

## Expected Output

The system can:

- Detect multiple supermarket products in one image
- Identify the detected product class
- Draw bounding boxes around detected products
- Display confidence scores for each detection

---

## Dataset & Model Used

The project uses supermarket product images from public datasets such as Roboflow and Kaggle.

The dataset contains approximately 10,000 supermarket product images.

Because of the large dataset size, the full dataset is not included in this GitHub repository. Instead, the repository contains sample test images, prediction results, model weights, and evaluation results.

A pretrained and fine-tuned YOLO model was used for object detection.

The model supports more than 100 supermarket-related product classes, including:

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
- Beans
- Broccoli
- Pineapple
- Strawberries
- Onion
- Corn

---

## Workflow / Architecture

Input Image  
↓  
Image Preprocessing  
↓  
YOLO Object Detection Model  
↓  
Object Detection  
↓  
Product Classification  
↓  
Bounding Boxes + Confidence Scores  
↓  
Final Output Image

---

## Results & Evaluation

The model was evaluated using object detection metrics.

At a confidence threshold of 10%, the model achieved:

- Precision: 36.5%
- Recall: 47.3%
- F1 Score: 37.7%
- mAP@50: 50.8%
- mAP@50:95: 34.3%
- mAP@75: 41.1%

Additional object-size evaluation results:

- Small objects mAP@50: 49.4%
- Medium objects mAP@50: 64.5%
- Large objects mAP@50: 43.5%

The confusion matrix and performance-by-class analysis show that the model performs better on some product classes than others.

---

## Model Comparison

Two YOLO26 model variants were compared on the test set: YOLO26s and YOLO26 Nano.

| Metric | YOLO26s | YOLO26 Nano |
|---|---:|---:|
| mAP@50 | 50.8% | 38.3% |
| Precision | 36.5% | 31.6% |
| Recall | 47.3% | 35.1% |
| F1 Score | 37.7% | 28.4% |

YOLO26s achieved higher performance across all major evaluation metrics.

Compared with YOLO26 Nano, YOLO26s improved:

- mAP@50 by 12.5 percentage points
- Precision by 4.9 percentage points
- Recall by 12.2 percentage points
- F1 Score by 9.3 percentage points

Based on the test-set results, YOLO26s was selected for the final supermarket product detection system because it provided stronger detection performance.

## Sample Prediction Results

The model was tested on four supermarket images.

### Coffee Shelf

- Detected 33 Coffee products
- Confidence scores ranged approximately from 0.40 to 0.86
- This was one of the strongest successful prediction examples

### Cheese Shelf

- Detected 21 Cheese objects
- Detected 3 Meat objects
- Detected 1 Yogurt object
- Highest confidence reached 0.95

### Fruit Image

- Detected 2 Apples
- Also predicted Avocado, Nectarine, and Plum
- Confidence scores were generally lower, ranging approximately from 0.26 to 0.62
- This image demonstrates class confusion between visually similar fruits

### Crowded Shelf

- Detected 59 Beans objects
- Confidence scores ranged approximately from 0.26 to 0.87
- The image demonstrates possible over-classification in crowded scenes

---

## Successful Prediction

The coffee shelf image is a successful prediction example.

The model detected 33 Coffee products with confidence scores reaching up to 0.86.

The cheese shelf image also produced strong detections, with Cheese predictions reaching a confidence score of 0.95.

These results show that the model performs well when product appearance is clear and consistent.

---

## Failure Case

The fruit image demonstrates a failure case.

The model detected some apples correctly, but also classified similar-looking fruits as:

- Avocado
- Nectarine
- Plum

The confidence scores in this image were generally lower, approximately between 0.26 and 0.62.

Another failure occurred in a crowded supermarket shelf image where many objects were classified as Beans.

These errors may occur because of:

- Similar colors and shapes between products
- Crowded shelves
- Overlapping objects
- Small object sizes
- Different lighting conditions
- Similar product packaging
- Duplicate or inconsistent class labels

---

## Deployment / Optimization

The YOLO model was exported from PyTorch format to ONNX format.

The exported file is:

`weights.onnx`

ONNX can be used to deploy the model on different platforms and environments.

Possible real-world applications include:

- Inventory monitoring
- Shelf monitoring
- Smart checkout systems
- Mobile supermarket applications
- Automatic stock detection
- Product counting

---

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

---

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt