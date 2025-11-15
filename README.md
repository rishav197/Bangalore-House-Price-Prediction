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

**Processing Location Feature(Categorical) :** 
Since the dataset contains many unique locations, similar or rare locations were grouped/reduced to avoid high dimensionality and improve model performance.

**Removing Outliers Using Domain Knowledge :**
- Properties with unrealistic square footage per BHK (e.g., less than 300 sqft per bedroom) were flagged as invalid and removed.

- This ensures we only keep properties that align with realistic housing standards (e.g., a 2 BHK should be at least ~600 sqft).

**Removing Inconsistent Pricing Within Each Location :**
- For each location, price-per-square-foot statistics were computed for every BHK category.

- Properties whose pricing contradicted typical patterns (e.g., a 3 BHK cheaper per sqft than a 2 BHK in the same location) were removed as inconsistent data points.

- Hello
    - How 
        * are
            + you?



