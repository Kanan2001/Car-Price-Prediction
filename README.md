This project involves developing a machine learning model to accurately predict used car prices. The final model is deployed in a Streamlit web app, where users can enter car details and receive instant price estimates.

Key Features:

Data Cleaning & Preprocessing: Removed unnecessary columns, handled missing data, detected and removed outliers, and encoded categorical features.
Feature Selection: Used a Random Forest Regressor to select the 15 most relevant features for predicting car prices.
Model Development: Trained multiple models, including Linear Regression, Decision Tree, Random Forest, and Gradient Boosting.
Model Evaluation: Compared models based on MAE, MSE, and R². The Gradient Boosting model performed best with the highest accuracy.
Model Deployment: Implemented a Streamlit app for real-time price predictions.
Visualization: Created feature importance plots and correlation heatmaps to understand feature relationships and model insights.
Model Performance Summary:

Gradient Boosting (Tuned) achieved the highest accuracy with an R² score of 0.9564, making it the best model for this task.
Results and Insights:

Feature Importance highlights key factors affecting car prices.
Correlation Heatmap shows relationships between different features.
Conclusion: The Tuned Gradient Boosting Regressor is the most accurate model for predicting used car prices, and the Streamlit app makes this accessible for real-time predictions.
