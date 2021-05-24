import pickle
import json
import numpy as np
file_path = 'Model/banglore_home_prices_model1.pickle'
model = pickle.load(open(file_path,'rb'))

class LinearRegressionModel():
    def get_location_names(self):
        with open("Model/columns1.json", "r") as f:
            locations_list = json.load(f)['data_columns']
        return locations_list

    def get_predicted_price(self,location,sqft,bath,bhk):
        with open("Model/columns1.json", "r") as f:
            data_columns = json.load(f)['data_columns']
            locations_list = data_columns  # first 3 columns are sqft, bath, bhk
            
        location = location.lower()
        loc_index = locations_list.index(location)
        x = np.zeros(len(locations_list))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        x[loc_index] = 1  # x[4] = 1
        print("*************************************************")
        return model.predict([x])[0]

if __name__ == "__main__":
    lr = LinearRegressionModel()
    price  = lr.get_predicted_price('Chikka Tirupathi',2600, 5, 4)
    print("The Predicted price is :",price)