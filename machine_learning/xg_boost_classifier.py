# XG Boost Classifier Example

#pip install xgboost   # run only for first time if you don't have xgboost

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt


def main():

    """
    XG Boost Classifier Example using sklearn function.
    Iris type dataset is used to demonstrate Classification algorithm.
    """

    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    X = iris["data"]  # features
    Y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    # Random Forest Classifier
    XGB_model = XGBClassifier()
    XGB_model.fit(x_train, y_train)

    # Display Confusion Matrix of XGBClassifier
    plot_confusion_matrix(
        XGB_model,
        x_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    main()
