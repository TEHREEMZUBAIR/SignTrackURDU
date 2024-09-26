---

# 📘 **SignTrackURDU: Urdu Sign Language Recognition and Translation**

### **Welcome to SignTrackURDU** 👋  
A state-of-the-art project to recognize and translate **Urdu Sign Language** using **computer vision** and **machine learning** technologies. This project allows you to collect data for hand gestures, train a model to recognize these gestures, and deploy the model to predict Urdu sign language symbols in real time. It is a step toward making communication easier and more accessible for the hearing-impaired community.

---

## 📝 **Table of Contents**
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation and Setup](#installation-and-setup)
- [Data Collection](#data-collection)
- [Model Training](#model-training)
- [Real-time Sign Language Detection](#real-time-sign-language-detection)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 **Project Overview**
SignTrackURDU recognizes and translates **Urdu Sign Language (USL)** using **OpenCV**, **Mediapipe**, and **TensorFlow**. The primary focus is on recognizing common letters and words of the Urdu alphabet. This project consists of:
- **Data Collection**: Capture images of hand gestures for various Urdu letters.
- **Model Training**: Train a deep learning model using the collected data.
- **Prediction**: Real-time recognition of Urdu sign gestures with visual feedback.

---

## 🧰 **Tech Stack**

**Languages & Frameworks:**
- 🐍 **Python**  
- 👁️ **OpenCV** for computer vision.
- ✋ **Mediapipe** for hand landmark detection.
- 🤖 **TensorFlow/Keras** for machine learning.
  
**Tools:**
- 🖥️ **Jupyter Notebook** for developing and testing code.
- 📊 **NumPy** and **Pandas** for data manipulation.
- 📂 **Mediapipe** for hand gesture detection.
- 📉 **Scikit-learn** for model evaluation and splitting data.

---

## 🔥 **Features**

1. **Data Collection**: Collect and store sign language images from a webcam.
2. **Hand Detection**: Uses **Mediapipe** to detect hand gestures in real time.
3. **Model Training**: Train a custom deep learning model with **LSTM layers**.
4. **Real-Time Prediction**: Recognize and predict Urdu hand signs with visual feedback.
5. **Customizable**: Easily expand the dataset by adding more Urdu sign gestures.

---

## 🗂️ **Directory Structure**

```
SignTrackURDU/
│
├── Image/                         # Directory for storing images of gestures.
├── MP_Data/                       # Directory for saving preprocessed data (keypoints).
├── Logs/                          # Directory for TensorBoard logs.
├── collectdata.py                 # Script for collecting sign images.
├── data.py                        # Script to preprocess images and extract keypoints.
├── train_model.py                 # Script to train the LSTM model.
├── app.py                         # Script for real-time sign language detection.
├── function.py                    # Helper functions for the project.
├── model.json                     # Saved model architecture.
├── model.h5                       # Trained model weights.
├── README.md                      # Project description (this file).
└── requirements.txt               # Required Python libraries.
```

---

## 🚀 **Installation and Setup**

### Step 1: Clone the Repository  
```bash
git clone https://github.com/your-username/SignTrackURDU.git
cd SignTrackURDU
```

### Step 2: Create and Activate a Virtual Environment  
```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### Step 3: Install the Required Dependencies  
```bash
pip install -r requirements.txt
```

---

## 📸 **Data Collection**

### Purpose:  
To collect hand gesture images of Urdu sign language symbols for training purposes.

### How to Use:
1. **Run the Script**:  
   ```bash
   python collectdata.py
   ```
2. **Instructions**:
   - Use the camera feed to place your hand inside the marked **Region of Interest (ROI)**.
   - **Press the corresponding letter key** to capture images for that Urdu sign.
   - Example: Press **‘A’** for **‘Alif’**, **‘B’** for **‘Bey’**, and so on.
   - **Press ‘ESC’** to stop data collection.

---

## 🧠 **Model Training**

### Purpose:  
To train a machine learning model on the collected gesture data using **LSTM layers** for time-sequence predictions.

### How to Use:
1. **Run the Training Script**:  
   ```bash
   python train_model.py
   ```
2. **Model Details**:
   - Input: 3D sequence of keypoints representing hand positions.
   - Layers: 3 **LSTM** layers followed by **Dense** layers.
   - Output: Prediction of Urdu sign gestures.

3. **Training Logs**:  
   Training logs are stored in the **Logs/** directory. You can view them using **TensorBoard**:
   ```bash
   tensorboard --logdir=Logs/
   ```

---

## 🎥 **Real-Time Sign Language Detection**

### Purpose:  
Use the trained model to predict Urdu sign language symbols in real time.

### How to Use:
1. **Run the Real-Time Prediction Script**:  
   ```bash
   python app.py
   ```
2. **Instructions**:
   - The webcam will open and show a live feed with a marked **ROI**.
   - As you perform gestures within the ROI, the model will predict and display the recognized Urdu sign.
   - The recognized gesture and its **confidence score** will be shown on the screen.
   - **Press ‘q’** to exit.

---

## 🤝 **Contributing**

We welcome contributions to improve SignTrackURDU! Feel free to submit pull requests, report issues, or suggest features.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## 📜 **License**

This project is licensed under the **MIT License**. Feel free to use it as you like, but please give credit! 😊

---

**Enjoy using SignTrackURDU to bridge communication gaps! 🙌💬**

---
