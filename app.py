import pickle
import pandas as pd
import streamlit as st
from PIL import Image

with open('diabetes','rb') as f:
    model = pickle.load(f)

def main():
     img = Image.open('diab.jpg')
     st.image(img)
     st.header('AI BASED DIABETES DIAGNOSIS')
     Pregnancies = st.text_input('NO. OF PREGNANCIES : ')
     Glucose = st.text_input('GLUCOSE LEVEL : ')
     BloodPressure = st.text_input('BLOOD PRESSURE : ')
     SkinThickness = st.text_input('SKIN THICKNESS : ')
     Insulin = st.text_input('INSULIN LEVEL : ')
     BMI = st.text_input('BMI : ')
     DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction : ')
     Age = st.text_input('AGE :') 

     df= pd.DataFrame(
        {
            'Pregnancies':[Pregnancies],
            'Glucose': [Glucose],
            'BloodPressure':[BloodPressure],
            'SkinThickness':[SkinThickness],
            'Insulin':[Insulin],
            'BMI':[BMI],
            'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
            'Age':[Age]
        }
     )
     if st.button('PREDICT'):
        result = model.predict(df)
        if(result==1):
            st.error('Patient is diabetic.')
        else:
            st.success('Patient is diabetes free.')

if __name__ == '__main__':
    main()