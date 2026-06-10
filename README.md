# Machine Learning Projects

A collection of Machine Learning, Data Analysis, and Data Visualization projects built using Python and popular Data Science libraries. This repository demonstrates end-to-end machine learning workflows including data preprocessing, exploratory data analysis (EDA), model development, evaluation, and model deployment preparation.

---

## Repository Structure

```text
Machine-Learning-Projects/
│
├── datasets/
│   ├── imdb-videogames.csv
│   ├── Callifornia housing.csv
│   ├── heart.csv
│   ├── Life Expectancy Data.csv
│   ├── Pass-Fail Data.csv
│   └── car_prediction_data.csv
│
├── imdb-videogames.ipynb
├── California_Housing_Prices.ipynb
├── heart_model.ipynb
├── Global Life Expectancy.ipynb
├── student_performance_prediction.ipynb
├── car_price_prediction.ipynb
│
├── requirements.txt
└── README.md
```

---

## Project Portfolio

| Project                             | Category                  | Algorithm               |
| ----------------------------------- | ------------------------- | ----------------------- |
| IMDb Video Games Analysis           | Exploratory Data Analysis | Data Analysis           |
| California Housing Price Prediction | Regression                | Linear Regression       |
| Heart Disease Prediction            | Classification            | Machine Learning        |
| Global Life Expectancy Analysis     | Exploratory Data Analysis | Data Analysis           |
| Student Performance Prediction      | Classification            | Logistic Regression     |
| Car Price Prediction                | Regression                | Random Forest Regressor |

---

# Projects Included

## 1. IMDb Video Games Analysis

**Notebook:** `imdb-videogames.ipynb`

This project analyzes IMDb ratings and metadata for video games to identify trends and insights.

### Tasks Performed

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Statistical analysis
* Data visualization
* Rating trend analysis

### Dataset

`datasets/imdb-videogames.csv`

---

## 2. California Housing Price Prediction

**Notebook:** `California_Housing_Prices.ipynb`

This project predicts California housing prices using regression techniques and housing-related features.

### Tasks Performed

* Data preprocessing
* Feature engineering
* Model training
* Performance evaluation
* Housing price prediction

### Dataset

`datasets/Callifornia housing.csv`

---

## 3. Heart Disease Prediction

**Notebook:** `heart_model.ipynb`

This project predicts whether a patient is at risk of heart disease using machine learning classification techniques.

### Tasks Performed

* Data cleaning and preprocessing
* Exploratory Data Analysis
* Feature selection
* Model training and evaluation
* Interactive prediction interface using Gradio

### Dataset

`datasets/heart.csv`

---

## 4. Global Life Expectancy Analysis

**Notebook:** `Global Life Expectancy.ipynb`

This project explores factors affecting life expectancy across countries.

### Tasks Performed

* Data cleaning
* Exploratory Data Analysis
* Data visualization
* Correlation analysis
* Trend identification

### Dataset

`datasets/Life Expectancy Data.csv`

---

## 5. Student Performance Prediction

**Notebook:** `student_performance_prediction.ipynb`

This project predicts whether a student will pass or fail based on academic performance and study habits.

### Problem Statement

Predict student performance using:

* Attendance Percentage
* Homework Percentage
* Midterm Score
* Study Hours Per Week

### Target Variable

* Pass = 1
* Fail = 0

### Tasks Performed

* Data collection and loading
* Exploratory Data Analysis (EDA)
* Data visualization
* Data preprocessing
* Feature scaling using StandardScaler
* Logistic Regression model training
* Performance evaluation
* Model saving using Pickle
* Student performance prediction

### Visualizations

* Histogram
* Boxplot
* Count Plot
* Scatter Plot
* Correlation Heatmap
* Pair Plot

### Model Used

* Logistic Regression

### Evaluation Metrics

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* Classification Report

### Dataset

Student Pass/Fail Dataset

### Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Pickle

---

## 6. Car Price Prediction

**Notebook:** `car_price_prediction.ipynb`

This project predicts the selling price of used cars using machine learning regression techniques.

### Problem Statement

Estimate the selling price of a vehicle using:

* Present Price
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission Type
* Owner Count
* Car Age

### Tasks Performed

* Data loading and cleaning
* Missing value analysis
* Duplicate removal
* Feature engineering
* Data preprocessing
* Model training
* Performance evaluation
* Feature importance analysis
* Model saving using Joblib

### Feature Engineering

Created a new feature:

```python
Car_Age = Current Year - Manufacturing Year
```

### Model Used

* Random Forest Regressor

### Evaluation Metrics

* R² Score
* Mean Absolute Error (MAE)

### Visualizations

* Feature Importance Chart

### Dataset

`datasets/car_prediction_data.csv`

### Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib

---

## Technologies Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Gradio
* Pickle
* Joblib

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Omkarkoli727/Machine-Learning.git
cd Machine-Learning
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## Running the Projects

1. Open any notebook.
2. Run all cells sequentially.
3. Explore visualizations and model outputs.
4. For the Heart Disease Prediction project, run the notebook completely to launch the Gradio interface.

---

## Learning Outcomes

This repository demonstrates:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization
* Feature engineering
* Classification models
* Regression models
* Model evaluation techniques
* Model serialization
* Interactive machine learning applications

---

## Future Improvements

* Add more machine learning projects
* Deploy models using Streamlit
* Add model comparison studies
* Improve documentation and testing
* Create end-to-end machine learning pipelines

---

## Author

Omkar Koli
