# from setuptools import find_packages, setup


# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Credit Risk Model code structuring',
#     author='Leonard Umoru',
#     license='',
# )
import pandas as pd
from src.data.make_dataset import load_data
# from src.visualization.visualize import plot_correlation_heatmap, plot_feature_importance, plot_confusion_matrix
from src.features.build_features import feature_eng
from src.models.train_model import train_lrmodel
from src.models.predict_model import eval_model
from src.visualization.visualize import  plot_market_trends

if __name__ == "__main__":
    # Load and preprocess the data
    data_path = "data/raw/real_estate.csv"
    df = load_data(data_path)

    # Create dummy variables and separate features and target
    x, y = feature_eng(df)

    # Train the linear regression model
    lrmodel, x_train, x_test, y_train, y_test = train_lrmodel(x, y)

    # Evaluate the model
    # plot_feature_importance(lrmodel, x)
    train_mae, test_mae = eval_model(lrmodel, x_train, x_test, y_train, y_test)
    
    # Visualizing real estate market trends
    df = pd.read_csv("data/processed/Processed_Real_Estate_Dataset.csv")
    # Add a 'property_type' column based on binary indicators
    df["property_type"] = df.apply(lambda row: "Bungalow" if row["property_type_Bunglow"] == 1 else "Condo", axis=1)
    plot_market_trends(df)
