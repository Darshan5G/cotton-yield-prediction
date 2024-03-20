import streamlit as st
import numpy as np

# Coefficients and intercept
coefficients = [-407.25063221,  399.19627636,   -5.52473231,    5.26072735, -1.93931005,  -20.90248094,   10.01411558,   -1.67743506, 49.70026605]
intercept = -1891.93474488

def predict_yield(x):
    # Calculate the predicted yield
    predicted_yield = intercept + np.dot(x, coefficients)
    return predicted_yield

def main():
    st.title('Cotton Yield Prediction')

    # Input features
    A = st.number_input('Area (ha)', format="%f", step=0.9)
    P = st.number_input('Production (kg)', format="%f", step=0.9)
    R = st.number_input('Annual Rainfall (mm)', format="%f", step=0.9)
    ST = st.number_input('Land Surface Temperature (K)', format="%f", step=0.9)
    FPAR = st.number_input('FPAR', format="%f", step=0.9)
    NDVI = st.number_input('NDVI', format="%f", step=0.9)
    LAI = st.number_input('LAI', format="%f", step=0.9)
    AT = st.number_input('Air Temperature(K)', format="%f", step=0.9)
    SM = st.number_input('Soil Moisture', format="%f", step=0.9)

    # Predict button
    predict_button = st.button('Predict', key="predict_button")

    if predict_button:
        # Input values as an array
        x_values = [np.log1p(A), np.log1p(P), np.log1p(R), np.log1p(ST), np.log1p(FPAR), np.log1p(NDVI), np.log1p(LAI), np.log1p(AT), np.log1p(SM)]
        x = np.array(x_values)
        
        # Predict yield
        result = predict_yield(x)
        
        # Display the result
        st.write(f'<div style="color: red; font-weight: bold; font-size: 24px;">The predicted yield is: {result:.3f} kg/ha</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
