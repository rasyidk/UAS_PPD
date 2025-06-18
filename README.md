# Chronic Kidney Disease Detection

This project is a final assignment (UAS) Praktikum Penamabangan Data for detecting **Chronic Kidney Disease (CKD)** using machine learning. It features a **web application built with Streamlit**, powered by a **Random Forest model** with **98% accuracy**, trained on a dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease).

## 🔍 Project Overview

Chronic Kidney Disease (CKD) is a condition characterized by a gradual loss of kidney function. Early detection is crucial. This project aims to help identify CKD using clinical parameters and machine learning.

### Features
- ✅ Input form for key medical parameters
- ✅ Real-time prediction (CKD or not CKD)
- ✅ Model built with Random Forest algorithm
- ✅ Model deployment with Streamlit
- ✅ Model serialized with `pickle`
- ✅ Achieved 98% accuracy on test data

## 🧠 Machine Learning

- **Model Used**: Random Forest Classifier
- **Accuracy**: 98%
- **Model Serialization**: `pickle`
- **Evaluation Metrics**: Accuracy, Confusion Matrix

## 📊 Dataset

- Base Source: UCI Machine Learning Repository - Chronic Kidney Disease
- Original Records: 400 data
- Extended Dataset: +200 additional data (manually added and cleaned based on original schema)
- Final Training Dataset Size: ±600 records
- Target: Predicted risk probability of having Chronic Kidney Disease (CKD), displayed as a percentage.

### Main Features Used:
| Parameter               | Description                    |
|-------------------------|--------------------------------|
| age                    | Age                            |
| bp                     | Blood pressure                 |
| sg                     | Specific gravity               |
| al                     | Albumin                        |
| su                     | Sugar                          |
| rbc                    | Red blood cells                |
| pc                     | Pus cell                       |
| pcc                    | Pus cell clumps                |
| ba                     | Bacteria                       |
| bgr                    | Blood glucose random           |
| bu                     | Blood urea                     |
| sc                     | Serum creatinine               |
| sod                    | Sodium                         |
| pot                    | Potassium                      |
| hemo                   | Hemoglobin                     |
| pcv                    | Packed cell volume             |
| wc                     | White blood cell count         |
| rc                     | Red blood cell count           |
| htn                    | Hypertension                   |
| dm                     | Diabetes mellitus              |
| cad                    | Coronary artery disease        |
| appet                  | Appetite                       |
| pe                     | Pedal edema                    |
| ane                    | Anemia                         |
