# Real_Estate_Price_Prediction
This app has been built using Streamlit and deployed with Streamlit community cloud

[Visit the app here](https://realestatesolutionwithapp-main-xpeymy7qyvfbak3qdsnnjx.streamlit.app/)

password - streamlit

This application predicts the price of a property based on its characteristics using a machine learning model trained on real estate data. Users can input various property details, and the model will predict the estimated price of the property.

## Features
- User-friendly interface powered by Streamlit.
- Input form to enter property details such as the year built, number of bedrooms and bathrooms, square footage, lot size, and other relevant factors.
- Real-time price prediction based on the trained model.
- Accessible via Streamlit Community Cloud.

## Dataset
The application is trained on a dataset of real estate transactions that include features like:
- Year built
- Number of bedrooms
- Number of bathrooms
- Square footage
- Lot size
- Property tax
- Insurance cost
- Whether the property has a basement
- Property type (Bungalow, Condo)
- Popularity of the property
- Whether it was sold during a recession

## Technologies Used
- **Streamlit**: For building the web application.
- **Scikit-learn**: For model training and evaluation.
- **Pandas** and **NumPy**: For data preprocessing and manipulation.
- **Matplotlib** and **Seaborn**: For exploratory data analysis and visualization (if applicable).

## Model
The predictive model is trained using real estate data. It applies preprocessing steps like encoding categorical variables and scaling numerical features. The classification model used here is Linear Regression, which predicts the property price based on the provided features.

## Future Enhancements
* Adding support for more advanced models such as Random Forest or XGBoost for better accuracy.
* Incorporating explainability tools like SHAP to provide insights into predictions.
* Adding visualizations to represent trends and relationships in property prices.

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mariemeba123/Real_Estate_Solution_with_Streamlit-main.git
   cd Real_Estate_Solution_with_Streamlit-main

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run app.py

#### Thank you for using the Real Estate Price Prediction Application! Feel free to share your feedback.
