
# python standard library
from collections import namedtuple

# third party
from sklearn import datasets

HousingData = namedtuple("HousingData", 'features prices names'.split())
def load_housing_data():
    """
    Convenience function to get the Boston housing data
    :return: housing_features, housing_prices
    """
    city_data = datasets.load_boston()
    return HousingData(features=city_data.data, prices=city_data.target,
                       names=city_data.feature_names)

CLIENT_FEATURES = [[11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24,
                    680.0, 20.20, 332.09, 12.13]]