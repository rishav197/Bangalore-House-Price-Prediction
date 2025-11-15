<!-- Project Title -->
# <div align="center">Bangalore House Price Prediction</div>


## Business Problem :

Real estate prices in Bangalore vary widely across locations and property features, making it difficult for buyers and sellers to estimate the fair market value of a home. This uncertainty often leads to mispricing, slower sales, or poor investment decisions.



### Objectives :

The goal is to build a machine learning model that predicts house prices in Bangalore using features like area size (in sqft), number of BHKs, number of bathrooms, and location. By providing accurate price estimates, the model helps buyers assess affordability and enables sellers to set competitive, data-driven listing prices.


## Dataset :

**Bengaluru House Price Data :** [Download Dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)


The dataset used in this project included information about :

Total sqft: Total area of the property in square feet
BHK: Number of bedrooms, halls, and kitchens
Bath: Number of bathrooms
Price: Price of the property (dependent variable)



## EDA and Data Preprocessing : 

### **Handling Missing Values :**
Identified and filled/removed missing entries to ensure clean and reliable data for training.

### **Processing Location Feature(Categorical) :** 
Since the dataset contains many unique locations, similar or rare locations were grouped/reduced to avoid high dimensionality and improve model performance.

### **Removing Outliers Using Domain Knowledge :**
- Properties with unrealistic square footage per BHK (e.g., less than 300 sqft per bedroom) were flagged as invalid and removed.

- This ensures we only keep properties that align with realistic housing standards (e.g., a 2 BHK should be at least ~600 sqft).

### **Removing Inconsistent Pricing Within Each Location :**
- For each location, price-per-square-foot statistics were computed for every BHK category.

- Properties whose pricing contradicted typical patterns (e.g., a 3 BHK cheaper per sqft than a 2 BHK in the same location) were removed as inconsistent data points.



## Model Building : 

To predict house prices in Bangalore, multiple machine learning models were trained and evaluated:

- Linear Regression – Used as a simple, interpretable baseline model to understand core relationships in the data.

- Lasso Regression – Applied to reduce overfitting and automatically select the most important features.

- Decision Tree Regressor – Used to capture non-linear patterns and complex interactions between features.


**Evaluation Metrics Used :**
- Mean Absolute Error (MAE) : Measures how much variance in the target variable is explained by the model.
- Root Mean Squared Error (RMSE) : Shows the average absolute difference between actual and predicted prices.
- R^2 Score : Penalizes larger errors and helps evaluate overall prediction accuracy. 


## Model Evaluations and Predictions : 

![model performances](https://github.com/rishav197/Bangalore-House-Price-Prediction/blob/main/model/model_performances.png)
> Based on the evaluation metrics, Linear Regression clearly performs the best among all models, providing the lowest error values and the highest R² score. This makes it the most accurate and stable model for predicting house prices in Bangalore. 



### Predictions :
> sample_input1 = { 'location': '1st Phase JP Nagar', 'sqft': 1000,  'bhk': 2, 'bath': 2}
>![sample_input data](https://github.com/rishav197/Telecom-Customer-Churn-Analysis-and-Prediction/blob/main/plots-and-images/example_input.jpg)


>sample_input2 = { 'location': 'Indira Nagar', 'sqft': 1000,  'bhk': 3, 'bath': 3}
>![sample_input data](https://github.com/rishav197/Telecom-Customer-Churn-Analysis-and-Prediction/blob/main/plots-and-images/example_input.jpg)



## Conclusion :

In this project, we analyzed the Bengaluru housing dataset to understand the factors influencing house prices, such as location, total sqft, number of BHKs, and bathrooms. After performing data cleaning, handling missing values, and removing outliers, we trained multiple machine learning models including Linear Regression, Lasso Regression, and Decision Tree Regressor. Based on evaluation metrics, Linear Regression emerged as the best model, achieving MAE = 18.58, RMSE = 34.81, and R² = 0.845, providing the most accurate and stable predictions. This model can help buyers assess affordability and assist sellers in setting competitive, data-driven property prices in Bangalore.



