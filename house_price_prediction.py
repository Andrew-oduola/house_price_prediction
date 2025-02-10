import pickle
import numpy as np
import streamlit as st
from PIL import Image

def predict(input_data):
    with open('house_price_pred_model.pkl', 'rb') as file:
        model = pickle.load(file)

    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting the one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -2)


    prediction = model.predict(input_data_reshaped)
    return prediction

def main():
    # Custom CSS for styling the title and "Created by" section
    st.markdown("""
    <style>
    .title {
        font-size: 36px !important;
        font-weight: bold !important;
        color: #4CAF50 !important;
        text-align: center;
        margin-bottom: 20px;
    }
    .created-by {
        font-size: 18px !important;
        font-style: italic;
        color: #555555;
        text-align: center;
    }
    .profile-pic {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin: 10px auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with custom design
    st.markdown('<p class="title">House Price Prediction App</p>', unsafe_allow_html=True)

    # Create a sidebar for "Created by" and profile picture
    with st.sidebar:
        st.markdown('<p class="created-by">Created by Andrew O.A.</p>', unsafe_allow_html=True)
        
        # Load and display your profile picture
        profile_pic = Image.open("prof.jpeg")  # Replace with your image file path
        st.image(profile_pic, caption="Andrew O.A.", use_container_width=True, output_format="JPEG", width=100)

    # App description
    st.write("""
    This app predicts the price of a house based on the features.
    Please fill in the details below and click **Predict**.
    """)

    # **Prediction placeholder (this will appear above the input fields)**
    result_placeholder = st.empty()


    # Create a two-column layout for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        area = st.number_input("Area of the house (in sqft)", value=3121, help="Area of the house in square feet")
        bedrooms = st.number_input("Number of bedrooms", value=4, help="Number of bedrooms in the house")
        bathrooms = st.number_input("Number of bathrooms", value=2, help="Number of bathrooms in the house")
        stories = st.number_input("Number of floors (stories)", value=2, help="Number of floors in the house (stories)")

    with col2:
        parking = st.number_input("Number of parking spaces", value=2, help="Number of parking spaces in the house")
        mainroad = st.selectbox("Mainroad", ["Yes", "No"], help="Is the house located near the main road?")
        guestroom = st.selectbox("Guestroom", ["Yes", "No"], help="Does the house have a guest room?")
        basement = st.selectbox("Basement", ["Yes", "No"], help="Does the house have a basement?")
        
    with col3:    
        hotwaterheating = st.selectbox("Hot water heating", ["Yes", "No"], help="Does the house have hot water heating?")
        airconditioning = st.selectbox("Air conditioning", ["Yes", "No"], help="Does the house have air conditioning?")
        prefarea = st.selectbox("Preferred area", ["Yes", "No"], help="Is the house located in a preferred area?")
        furnishingstatus = st.selectbox("Furnishing status", ["Semi-furnished", "Unfurnished", "Furnished"], help="Furnishing status of the house")


    # Convert categorical data to numerical data    
    mainroad = 1 if mainroad == "Yes" else 0
    guestroom = 1 if guestroom == "Yes" else 0
    basement = 1 if basement == "Yes" else 0
    hotwaterheating = 1 if hotwaterheating == "Yes" else 0
    airconditioning = 1 if airconditioning == "Yes" else 0
    prefarea = 1 if prefarea == "Yes" else 0
    furnishingstatus = 1 if furnishingstatus == "Furnished" else (2 if furnishingstatus == "Semi-furnished" else 0)
    
    # Combine all input data into a single list
    input_data = [area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]

    # When the "Predict" button is clicked, make the prediction and display the result
    if st.button("Predict"):
        prediction = predict(input_data)
        # st.header("Prediction Result:")
        # print(prediction)
        result_placeholder.success(f"Predicted House Price: ${prediction[0]:,.2f}")
        st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
        # st.success(f"Predicted House Price: ${prediction[0]:,.2f}")

    st.sidebar.title("About")
    st.sidebar.info("This app uses a machine learning model to predict house price.")
    st.sidebar.markdown("[GitHub](https://github.com/Andrew-oduola) | [LinkedIn](https://linkedin.com/in/andrew-oduola-django-developer)")


if __name__ == '__main__':
    main()
