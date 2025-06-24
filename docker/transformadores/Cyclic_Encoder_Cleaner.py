from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class CyclicEncoderCleaner(BaseEstimator, TransformerMixin):
    """
    Esta clase convierte variables cíclicas (por ejemplo, mes o día) en una representación continua.
    Aplica transformaciones seno y coseno para capturar la naturaleza circular de estas variables.
    Esto ayuda a los modelos a entender la proximidad entre valores como diciembre y enero.
    """
    def __init__(self):
        self.wind_dir_map = {
            'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5, 'E': 90,
            'ESE': 112.5, 'SE': 135, 'SSE': 157.5, 'S': 180, 'SSW': 202.5,
            'SW': 225, 'WSW': 247.5, 'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
        }

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_ = X.copy()

        # Direcciones a grados
        X_['WindGustDir_degrees'] = X_['WindGustDir'].map(self.wind_dir_map)
        X_['WindDir9am_degrees'] = X_['WindDir9am'].map(self.wind_dir_map)
        X_['WindDir3pm_degrees'] = X_['WindDir3pm'].map(self.wind_dir_map)

        # Codificación cíclica
        for col in ['WindGustDir', 'WindDir9am', 'WindDir3pm']:
            deg_col = col + '_degrees'
            X_[f'{col}_sin'] = np.sin(2 * np.pi * X_[deg_col] / 360)
            X_[f'{col}_cos'] = np.cos(2 * np.pi * X_[deg_col] / 360)

        # Codificación cíclica para mes
        X_['mes_sin'] = np.sin(2 * np.pi * X_['mes'] / 12)
        X_['mes_cos'] = np.cos(2 * np.pi * X_['mes'] / 12)

        # Columnas a eliminar
        cols_drop = [
            'WindGustDir_degrees', 'WindGustDir',
            'WindDir9am', 'WindDir9am_degrees',
            'WindDir3pm', 'WindDir3pm_degrees',
            'mes', 'Evaporation', 'Rainfall', 'fecha',
            'MinTemp', 'MaxTemp', 'WindGustSpeed', 'WindSpeed9am',
            'WindSpeed3pm', 'Humidity9am', 'Pressure9am', 'Pressure3pm',
            'Temp9am', 'Temp3pm',
            'WindGustSpeed_log', 'WindSpeed9am_log', 'WindSpeed3pm_log', 'Date', 'Latitude', 'Longitude', 'Location'
        ]

        X_ = X_.drop(columns=[col for col in cols_drop if col in X_])
        return X_
