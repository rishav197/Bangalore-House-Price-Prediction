import pickle
import json
import numpy as np


import warnings
# Hide all warnings
warnings.filterwarnings('ignore')


__locations = None
__data_columns = None
__model = None 



def load_saved_artifacts():
    print('loading saved artifacts has been started.......')
    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_cols']
        __locations = __data_columns[3:]


    with open('./artifacts/best_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    

    print('loading saved artifacts has been Done.......')


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


def get_estimated_price(location, sqft, bhk, bath):
    
    try:
        loc_idx = __data_columns.index(location.lower())
    except:
        loc_idx = -1
    # print(loc_idx, __locations[loc_idx-3])

    Xq = np.zeros(len(__data_columns))
    Xq[0] = sqft
    Xq[1] = bath
    Xq[2] = bhk

    if loc_idx >= 0:
        Xq[loc_idx] = 1

    # print(Xq)
    return round(__model.predict([Xq])[0], 2)


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location_names())
    # print(get_data_columns)

    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('Indira Nagar', 1000, 2, 2))

