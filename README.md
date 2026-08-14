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



# 📊 Student Performance Analysis

## 📌 Project Overview
This project focuses on analyzing student performance using Python and data visualization techniques.
The analysis explores students' **math, reading, and writing scores** and examines relationships between scores, gender, and parental level of education.

## 🎯 Objectives
- Load and explore the student performance dataset
- Check the dataset structure and missing values
- Generate statistical summaries
- Analyze the distribution of math scores
- Study the relationship between reading and writing scores
- Compare average scores by gender
- Analyze the relationship between parental education and math scores
- Study the correlation between math, reading, and writing scores


## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Google Colab


## 📂 Project Structure
Student-Performance-Analysis/
│
├── StudentsPerformance.csv
├── student_performance.py
└── README.md

# 📊 Dataset
The project uses the StudentsPerformance.csv dataset.
The analysis uses student performance variables including:
math Score
Reading Score
Writing Score
Gender
Parental Level of Education

# 🔍 Data Analysis
1. Dataset Exploration
The dataset is loaded using Pandas and the first few records are displayed.
Missing values are also checked, along with descriptive statistics such as:
Count
Mean
Standard deviation
Minimum
Maximum
Quartiles

# 📈 Visualizations
The project includes the following visualizations:
math Score Distribution
A histogram is used to understand the distribution of students' math scores.

Reading vs Writing Scores
A scatter plot is used to analyze the relationship between reading and writing scores.

Average Scores by Gender
Average math, reading, and writing scores are calculated for each gender and displayed using a bar chart.

Parental Education vs Math Score
A box plot is used to examine the relationship between parental level of education and students' math scores.

Correlation Between Scores
A correlation heatmap is used to analyze the relationship between:
Math Score
Reading Score
Writing Score

# 🔄 Project Workflow
Load Dataset
      ↓
Data Exploration
      ↓
Check Missing Values
      ↓
Statistical Analysis
      ↓
Data Visualization
      ↓
Group Analysis
      ↓
Correlation Analysis
      ↓
Insights

# 📌 Key Analysis Areas
The project focuses on understanding:
Distribution of student scores
Relationship between reading and writing performance
Average performance by gender
Relationship between parental education and math performance
Correlation among math, reading, and writing scores

# ▶️ How to Run
1. Install required libraries
pip install pandas matplotlib seaborn
2. Place the dataset in the project folder
Make sure the following file is available:
StudentsPerformance.csv
3. Run the Python program
python student_performance.py

The program will display the dataset information, statistical analysis, and visualizations.

# 📌 Conclusion
This project demonstrates how Python can be used for data analysis and exploratory data visualization.
It provides a practical understanding of student performance by analyzing score distributions, relationships between subjects, gender-based averages, parental education, and correlations between scores.

# 👩‍💻 Author
# Lavanya Yalamanchi
# Computer Science & Data Science Student
