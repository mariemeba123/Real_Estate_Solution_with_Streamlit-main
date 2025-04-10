
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

def plot_market_trends(data):
    """
    Plot a  market trends for the given data.
    
    Args:
        data (pandas.DataFrame): The input data.
    """
    fig, ax2 = plt.subplots()
    sns.boxplot(data=data, x="property_type", y="price", ax=ax2)
    plt.xlabel("Property Type")
    plt.ylabel("Price ($)")
    plt.title("Price Distribution by Property Type")
    fig.savefig("market.png")

# def plot_feature_importance(lrmodel, x):
#     """
#     Plot a bar chart showing the feature importances.
    
#     Args:
#         feature_names (list): List of feature names.
#         feature_importances (list): List of feature importance values.
#     """
#     fig, ax = plt.subplots()
#     ax = sns.barplot(x=lrmodel.feature_importances_, y=x.columns)
#     plt.title("Feature importance chart")
#     plt.xlabel("Importance")
#     plt.ylabel("Feature")
#     plt.tight_layout()
#     fig.savefig("feature_importance.png")

# def plot_confusion_matrix(y_true, y_pred, classes, normalize=False, title='Confusion Matrix'):
#     """
#     Plot the confusion matrix for the given true and predicted labels.
    
#     Args:
#         y_true (numpy.ndarray): Array of true labels.
#         y_pred (numpy.ndarray): Array of predicted labels.
#         classes (list): List of class labels.
#         normalize (bool, optional): Whether to normalize the confusion matrix. Default is False.
#         title (str, optional): Title for the plot. Default is 'Confusion Matrix'.
#     """
#     cm = confusion_matrix(y_true, y_pred)
#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

#     plt.figure(figsize=(8, 6))
#     sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=classes, yticklabels=classes)
#     plt.xlabel('Predicted', fontsize=12)
#     plt.ylabel('Actual', fontsize=12)
#     plt.title(title, fontsize=16)
#     plt.show()