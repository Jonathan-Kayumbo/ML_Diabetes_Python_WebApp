# Import Libraries
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st

st.write(""" 
#Diabetes Detection

Detects if someone has diabetes using Machine Learning and Python 
""")

#Display image
image = Image.open('usr/src/app/diabetes.jpg')
st.image(image, caption='ML', use_column_width=True)

#Get The Data
df = pd.read_csv('usr/src/app/diabetes.csv')

#Set a SubHeader
st.subheader('Data Information:')

st.dataframe(df.describe())

#Show the data as a chart

chart = st.bar_chart(df)

#Split the dat into independet X and dependent Y variables

X = df.iloc[:, 0:8] .values
Y = df.iloc[:, -1] .values

#Split the dat set into 75% training and 25% Testing

X_train , X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

#Get the feature input the data

def get_user_input():
    pregnancies = st.sidebar.slider('pregnancies', 0, 17, 3)
    glucose = st.sidebar.slider('Glucose', 0, 199, 117)
    blood_pressure = st.sidebar.slider('Blood_Pressure', 0, 122, 72)
    skin_thickness = st.sidebar.slider('Skin_Thickness', 0, 99, 23)
    insulin = st.sidebar.slider('Insulin', 0.0, 846.0, 30.0)
    BMI = st.sidebar.slider('BIM', 0.0, 67.1, 32.0)
    DiabetesPedigreeFunction = st.sidebar.slider('Diadetes_Pedigree_Function', 0.078, 2.42, 0.3725)
    age = st.sidebar.slider('age', 21, 81, 29)

    #Store a dic into variables
    user_data = {
        'pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI':BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'age': age
    }
    #Transform the data into a dataframe
    features = pd.DataFrame(user_data, index=[0])
    return features

user_input = get_user_input()

#Set a subheader and display the user input
st.subheader('User Input:')
st.write(user_input)

#Create and train the model
RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train, Y_train)

#Show the model metrics
st.subheader('Model Test Accurancy Score:')
st.write(str(accuracy_score(Y_test, RandomForestClassifier.predict(X_test)) * 100)+'%')

#Store the model predictions in a variable

prediction = RandomForestClassifier.predict(user_input)

#Set a subheader and display the classification
st.subheader('Classification :')
st.write(prediction)
