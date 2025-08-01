import streamlit as st
import numpy as np

st.title("🏠 House Price Predictor")
st.write("Predict house prices using machine learning!")

st.sidebar.header("House Features")

overall_qual = st.sidebar.slider("Overall Quality (1-10)", 1, 10, 7)
gr_liv_area = st.sidebar.number_input("Ground Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.sidebar.selectbox("Garage Cars", [0, 1, 2, 3, 4])
year_built = st.sidebar.slider("Year Built", 1870, 2023, 2000)

if st.sidebar.button("🔮 Predict Price"):
    predicted_price = (gr_liv_area * 100) + (overall_qual * 15000) + (garage_cars * 10000) + (year_built * 50)
    st.success(f"🎯 Predicted Price: ${predicted_price:,.0f}")
    
    st.write("### Input Summary:")
    st.write(f"- **Overall Quality**: {overall_qual}/10")
    st.write(f"- **Living Area**: {gr_liv_area:,} sq ft")
    st.write(f"- **Garage**: {garage_cars} cars")
    st.write(f"- **Year Built**: {year_built}")