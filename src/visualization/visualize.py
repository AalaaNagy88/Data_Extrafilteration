from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.metrics import ConfusionMatrixDisplay

"""
    Args:
       clf: model object
       x_test: test_set
       y_test: true labels of the test
       y_pred: prediction of the test

    Return:
        classification report
        confusion matrix 
"""
def visualize_results(clf,x_test,y_test, y_pred):
    print("Classification report:\n", classification_report(y_test, y_pred))
    ConfusionMatrixDisplay.from_estimator(clf, x_test, y_test)  
