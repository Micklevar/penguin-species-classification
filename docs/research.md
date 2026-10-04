# Preliminary Project Research

## 1. What do I want to do?
I want to develop and evaluate a machine learning model capable of classifying penguin species with high performance based on their morphological characteristics, justifying the decisions made during the analysis, preprocessing, feature selection, training, and evaluation of the model.

## 2. Why did I choose this dataset?
The target is precisely a qualitative variable, meaning I have categories for the species. This allows me to apply classification algorithms. Additionally, I am interested in working with biological characteristics to potentially enter areas like aquaculture in the future.

## 3. Where does the data come from?
The data comes from Kaggle: [Palmer's Penguin Dataset Extended](https://www.kaggle.com/datasets/samybaladram/palmers-penguin-dataset-extended).

## 4. What does the data represent?
The data represents morphological variables of penguins, as well as variables related to their biology and ecology.

## 5. What penguin species appear?
There are 3 species:
* Adelie
* Chinstrap
* Gentoo

## 6. What does each feature mean?

| Feature | Meaning |
| :--- | :--- |
| **Island** | Island where the penguin was found |
| **Sex** | Gender of the penguin |
| **Diet** | Main diet of the penguin |
| **Year** | Year the data was collected |
| **Life Stage** | The penguin's life stage |
| **Body Mass** | Body mass in grams |
| **Bill Length** | Length of the bill in millimeters |
| **Bill Depth** | Depth of the bill in millimeters |
| **Flipper Length** | Length of the flipper in millimeters |
| **Health Metrics** | Health status of the penguin (healthy, overweight, underweight) |

## 7. What would my target variable be?
The target variable would be `Species`.

## 8. What questions do I want to answer?
I want to determine the species as accurately as possible, which means a prediction paradigm will be applied. Therefore, the questions to be answered are:

### EDA (Exploratory Data Analysis)
* What variables exist?
* Are they potentially useful?
* How are they distributed?
* Are there relationships between variables?
* Are there differences between species?
* Are there missing values?
* Are there outliers?
* Are there correlations?
* Are there quality issues?

### Preprocessing 
* How do I handle missing values if there are any?
* Do I need to transform variables?
* Do I need to scale the data?
* Do I need to encode categorical variables?
* Should I drop any variables?

### Modeling
* Does the problem seem linear?
* How flexible should the model be?
* Parametric or non-parametric?
* What are the candidate models?

### Evaluation
* Which model generalizes better?
* Which model performs best?
* Where does the model make mistakes?

## 9. What do I expect to find? 
I expect to identify which variables contain the most information to distinguish between species and determine which features contribute the most to the predictive performance of the models.

## 10. What problems could exist in the data?
* Variables poorly related to the target.
* Highly correlated variables (which probably won't add information to the model).
* Variables with skewed distributions.
* Variables with very different scales.
* Missing values.
* Outliers.
* Numerical variables that are actually categorical.