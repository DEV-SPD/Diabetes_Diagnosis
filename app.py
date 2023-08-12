import pickle
import pandas as pd
import streamlit as st
from PIL import Image

with open('diabetes','rb') as f:
    model = pickle.load(f)

def main():
     img = Image.open('diab.jpg')
     st.image(img)
     st.title('DIABETES DIAGNOSIS')
     col1,col2,col3 = st.columns(3)
     with col1:
      Age = st.text_input('AGE :')
      Pregnancies = st.text_input('NO. OF PREGNANCIES : ')
      Glucose = st.text_input('GLUCOSE LEVEL : ')
     with col2:
      BloodPressure = st.text_input('BLOOD PRESSURE : ')
      SkinThickness = st.text_input('SKIN THICKNESS : ')
      Insulin = st.text_input('INSULIN LEVEL : ')
     with col3:
      BMI = st.text_input('BMI : ')
      DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction : ')
       

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
            st.error('Diagnosis Result: Patient is diabetic.')
            st.info('FOLLOWING ARE SOME HEALTHCARE ADVISES:')
            st.info('1. Monitor Blood Sugar Levels: Regularly check your blood sugar levels as advised by your healthcare provider. Monitoring can help you understand how different foods, activities, and medications affect your blood sugar.')
            st.info('2. Healthy Eating: Follow a balanced and nutritious diet. Focus on whole grains, lean proteins, healthy fats, and a variety of fruits and vegetables. Limit your intake of sugary foods and refined carbohydrates.')
            st.info('3. Hydration: Stay hydrated by drinking plenty of water throughout the day. Avoid sugary beverages and excessive caffeine.')
            st.info('4. Sleep: Prioritize getting enough restful sleep each night, as lack of sleep can affect blood sugar control.')
            st.info('5. Blood Pressure Management: Keep your blood pressure under control, as high blood pressure can contribute to diabetes-related complications.')
            st.info('6. Cholesterol Control: Manage your cholesterol levels through a combination of a healthy diet, exercise, and, if necessary, medication.')
        else:
            st.success('Patient is diabetes free.')

if __name__ == '__main__':
    main()
