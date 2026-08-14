# Machine-Learning-Journey
A collection of Machine Learning projects developed using Python, covering data preprocessing, exploratory data analysis, visualization, feature scaling, model training, evaluation, and prediction. Projects use libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn to solve practical prediction and classification problems.


# 🎓 Placement Prediction using Machine Learning
## 📌 Project Overview
This project predicts whether a student is likely to be placed based on their **CGPA** and **IQ** using Machine Learning.
The project uses **Logistic Regression** as the classification algorithm and **StandardScaler** for feature scaling.

## 🎯 Objective
The main objective of this project is to build a Machine Learning model that predicts:
- **1 → Placed**
- **0 → Not Placed**
based on the student's:
- CGPA
- IQ

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Google Colab / Jupyter Notebook

## 📂 Project Structure
Placement-Prediction/
│
├── placement.csv
├── train_model.py
├── model.pkl
├── scaler.pkl
└── README.md

# File	Description
*placement.csv-	Dataset containing student CGPA, IQ and placement information
*train_model.py -	Complete Machine Learning training code
*model.pkl	 - Saved Logistic Regression model
*scaler.pkl -Saved StandardScaler
*README.md	- Project documentation

# 📊 Dataset
The dataset contains information about students and their placement status.

# 🔄 Machine Learning Workflow
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Data Visualization
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
StandardScaler
   ↓
Logistic Regression
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
Save Model

# 🧹 Data Cleaning
The dataset contains an unnecessary index column named:
Unnamed: 0
This column is removed before training the model.
Missing values are also checked using:
df.isnull().sum()

# 📈 Data Visualization
The project includes the following visualizations:

Placement Distribution
CGPA Distribution
IQ Distribution
CGPA vs Placement
IQ vs Placement
CGPA vs IQ
Correlation Heatmap

These visualizations help understand the relationship between student features and placement.

# 🤖 Machine Learning Algorithm
Logistic Regression
Logistic Regression is used because the project is a binary classification problem.
The model predicts two possible outcomes:

Placed
Not Placed

# ⚖️ Feature Scaling
StandardScaler is used to scale CGPA and IQ before training the Logistic Regression model.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 🧪 Train-Test Split
The dataset is divided into training and testing data using:
train_test_split(
    X,
    Y,
    test_size=0.1,
    random_state=2
)

The training data is used to train the model, while the testing data is used to evaluate its performance.

# 📊 Model Evaluation
The model is evaluated using:

# Accuracy
accuracy_score(Y_test, Y_pred)
Classification Report
classification_report(Y_test, Y_pred)

# The classification report provides:
Precision
Recall
F1-score
Support

# 🔮 Sample Prediction
The trained model can be tested with a new student's CGPA and IQ.
Example:
CGPA = 8.0
IQ = 110

The model predicts whether the student is:

PLACED
or
NOT PLACED

# 💾 Saved Model Files
After training, two files are created.

# model.pkl
This file contains the trained Logistic Regression model.

# scaler.pkl
This file contains the fitted StandardScaler.
These files allow the trained model and scaler to be saved and reused without training the model again.

# ▶️ How to Run the Project
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the Project Folder
cd Placement-Prediction
3. Install Required Libraries
pip install pandas numpy matplotlib seaborn scikit-learn
4. Run the Python File
python train_model.py

# The program will:
Load the dataset
Clean the data
Check missing values
Display visualizations
Split the data
Scale the features
Train the Logistic Regression model
Calculate accuracy
Generate a classification report
Test a new student
Save model.pkl
Save scaler.pkl

# 📌 Conclusion
This project demonstrates a basic end-to-end Machine Learning workflow, starting from data loading and preprocessing to visualization, model training, evaluation, prediction, and model saving.

The project demonstrates how Logistic Regression can be used to predict student placement based on CGPA and IQ.

# 👩‍💻 Author
# Lavanya Yalamanchi
# Computer Science & Data Science Student
