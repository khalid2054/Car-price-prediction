import streamlit as st
import pickle
import pandas as pd


with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)
st.title('...CAR Price Prediction (FORD)')
st.markdown('provide details for car.......')

# numerical data
year = st.slider('year',min_value=1996, max_value=2020)
mileage = st.slider('Mileage',min_value=1.0, max_value=177644.0)
tax = st.slider('Tax',min_value=0, max_value=580)
EngineSize = st.slider('EngineSize',min_value=0.0, max_value=5.0)
MPG= st.slider('Mpg',min_value=20.800000, max_value=201.800000)


# categorical
fuel_type = st.selectbox('Fuel Type', options=['Electric', 'Hybrid', 'Other', 'Petrol'])

transmission = st.selectbox('Transmission', options=['Manual', 'Semi-Auto'])

model_name = st.selectbox('Car Model', options=[
    'C-MAX', 'EcoSport', 'Edge', 'Escort', 'Fiesta', 'Focus', 'Fusion',
    'Galaxy', 'Grand C-MAX', 'Grand Tourneo Connect', 'KA', 'Ka+',
    'Kuga', 'Mondeo', 'Mustang', 'Puma', 'Ranger', 'S-MAX', 'Streetka',
    'Tourneo Connect', 'Tourneo Custom', 'Transit Tourneo'
])

if st.button("Predict"):
    raw_input = {
        'year': year,
        'mileage': mileage,
        'tax': tax,
        'mpg': MPG,
        'engineSize': EngineSize,
        'fuelType_Electric': 1 if fuel_type == 'Electric' else 0,
        'fuelType_Hybrid': 1 if fuel_type == 'Hybrid' else 0,
        'fuelType_Other': 1 if fuel_type == 'Other' else 0,
        'fuelType_Petrol': 1 if fuel_type == 'Petrol' else 0,
        'transmission_Manual': 1 if transmission == 'Manual' else 0,
        'transmission_Semi-Auto': 1 if transmission == 'Semi-Auto' else 0,
        'model_ C-MAX': 1 if model_name == 'C-MAX' else 0,
        'model_ EcoSport': 1 if model_name == 'EcoSport' else 0,
        'model_ Edge': 1 if model_name == 'Edge' else 0,
        'model_ Escort': 1 if model_name == 'Escort' else 0,
        'model_ Fiesta': 1 if model_name == 'Fiesta' else 0,
        'model_ Focus': 1 if model_name == 'Focus' else 0,
        'model_ Fusion': 1 if model_name == 'Fusion' else 0,
        'model_ Galaxy': 1 if model_name == 'Galaxy' else 0,
        'model_ Grand C-MAX': 1 if model_name == 'Grand C-MAX' else 0,
        'model_ Grand Tourneo Connect': 1 if model_name == 'Grand Tourneo Connect' else 0,
        'model_ KA': 1 if model_name == 'KA' else 0,
        'model_ Ka+': 1 if model_name == 'Ka+' else 0,
        'model_ Kuga': 1 if model_name == 'Kuga' else 0,
        'model_ Mondeo': 1 if model_name == 'Mondeo' else 0,
        'model_ Mustang': 1 if model_name == 'Mustang' else 0,
        'model_ Puma': 1 if model_name == 'Puma' else 0,
        'model_ Ranger': 1 if model_name == 'Ranger' else 0,
        'model_ S-MAX': 1 if model_name == 'S-MAX' else 0,
        'model_ Streetka': 1 if model_name == 'Streetka' else 0,
        'model_ Tourneo Connect': 1 if model_name == 'Tourneo Connect' else 0,
        'model_ Tourneo Custom': 1 if model_name == 'Tourneo Custom' else 0,
        'model_ Transit Tourneo': 1 if model_name == 'Transit Tourneo' else 0,
        'model_Focus': 1 if model_name == 'Focus' else 0,
    }

    input_df = pd.DataFrame([raw_input])
    input_df = input_df[['year', 'mileage', 'tax', 'mpg', 'engineSize', 'model_ C-MAX',
       'model_ EcoSport', 'model_ Edge', 'model_ Escort', 'model_ Fiesta',
       'model_ Focus', 'model_ Fusion', 'model_ Galaxy', 'model_ Grand C-MAX',
       'model_ Grand Tourneo Connect', 'model_ KA', 'model_ Ka+',
       'model_ Kuga', 'model_ Mondeo', 'model_ Mustang', 'model_ Puma',
       'model_ Ranger', 'model_ S-MAX', 'model_ Streetka',
       'model_ Tourneo Connect', 'model_ Tourneo Custom',
       'model_ Transit Tourneo', 'model_Focus', 'fuelType_Electric',
       'fuelType_Hybrid', 'fuelType_Other', 'fuelType_Petrol',
       'transmission_Manual', 'transmission_Semi-Auto']]
    
    prediction = model.predict(input_df)
    st.success(f"Predicted Car Price: £{prediction[0]:,.2f}")