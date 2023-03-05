import streamlit as st
import pickle
from datetime import datetime, timedelta

def load():
    with open('model.pcl','rb') as fid:
        return pickle.load(fid)

model = load()

today = datetime.now(tz=None)
col1, col2 = st.columns(2)
with col1:
    birthday = st.date_input(
        "your birthday",
        today - timedelta(days = 365*10),
        min_value = today - timedelta(days = 365*100),
        max_value = today - timedelta(days = 365*10))

    age = today.toordinal() - birthday.toordinal()

    st.write('yuor age:', round(age/365))
with col2:
    gender = st.radio(
        "your gender",
        ('male', 'female'))

gender_code = {
   'male' : 2, 
   'female' : 1
}

height = st.slider('yuor height', 100, 250, 170)
weight = st.slider('yuor weight', 30, 250, 70)

ap_hi = st.slider('yuor upper blood pressure', 20, 200, 120) 
ap_lo = st.slider('yuor lower blood pressure', 20, 200, 70)

col3, col4, col5 = st.columns(3)

with col3:
    cholesterol  = st.radio(
        "your cholesterol",
        (1, 2, 3))
    
with col4:    
    gluc   = st.radio(
        "your glucose level",
        (1, 2, 3))

with col5:
    smoking = st.checkbox('do you smoke?') 
    smoke = 0 
    if smoking: smoke = 1
    
    alcohol = st.checkbox('do you drink alcohol?') 
    alco = 0 
    if alcohol: alco = 1

    sport = st.checkbox('do you play sports?') 
    active = 0 
    if sport: active = 1

result = model.predict_proba([[age, 
                               gender_code[gender], 
                               height, 
                               weight, 
                               ap_hi, 
                               ap_lo, 
                               cholesterol, 
                               gluc,
                               smoke,
                               alco,
                               active]])[:, 1][0]

st.header('your chance of heart disease: '+ str(round(result,2)))
