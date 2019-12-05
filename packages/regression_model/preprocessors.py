import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class CategoricalImputer(BaseEstimator(), TransformerMixin()):
    """
    categorical data missing value imputer

    Arguments:
        BaseEstimator {[type]} -- [description]
        TransformerMixin {[type]} -- [description]
    """

    def __init__(self, variable = None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def  fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'CategoricalImputer':
        """
        Fit statement to accomodate the sklearn pipeline
        """

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Apply the transorms to the data frame
        """
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X
