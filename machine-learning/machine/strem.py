import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
import datetime as dt


#marchine learning code
data=pd.read_csv('data/dada.csv')
x=data.drop(columns=['genre'])
y=data['genre']

#g=data.drop(columns=['age'])
#age=data['age']
#new=data['doubleage']=data['age']*2

module=DecisionTreeClassifier()
module.fit(x, y)


st.set_page_config(
     page_title='("promise").Simple marchine learning',
)
st.sidebar.title("Wolf Organisation. ") 
    
if 'view' is not st.session_state:
     st.session_state['view']=0 
st.session_state.view=st.sidebar.button("view data set")

min_date=dt.datetime(1790,1,1)
max_date=dt.datetime(9099,1,1)



form_value=["age","gender"]
title_one=st.title("simple machine learning project")
paragraph_one=st.write("This is a made up data of age, gender and their music prefarence." \
" The gender atribute is represented by 1 and 2 for MALE and FEMALE")
if st.session_state.view is True:
     st.session_state.view+=1
     st.dataframe(data)

#prediction_input
with st.form(key="input_prediction_form"):
    st.subheader("Input values ")
    form_value[0]=st.number_input("Age")
    form_value[1]=st.selectbox("Gender",["1","2"])
    prediction=module.predict([ [form_value[0],form_value[1]] ])

    btn=st.form_submit_button("predict")


    if form_value[0] and form_value[1] and btn == True:
        st.subheader(prediction)
        st.write("")
    else:
        st.subheader("sorry invalid data")


sub_heder=st.write("This code was writen by promise ndegwa ")
paragraph_two=st.subheader("This project was made and developd by The wolf Organisation")
#text area
if 'text' is not st.session_state:
     st.session_state['text']=0

with st.form(key="comunicat_form"):
    st.session_state.text=st.text_area ("send us your thoughts ")
    send=st.form_submit_button("send")

if st.session_state.text and send == True:
    st.session_state.text=0
    bj=st.success("Thank's for your thought's. ")
    st.balloons()

#join form
with st.expander("Data infomation"):   
    st.title("Music data info")
    st.write("This is a made up data of age, gender and their music prefarence." \
" The gender atribute is represented by 1 and 2 for MALE and FEMALE. This machine "
"learning app is a simulation of a real life situation. The algorithm used in the app is"
" DecisionTreeClassifier, the reason for using this module is becouse it'simple and fast"
"and good for small amount of data like the app is using. You can check out other marchine"
" learning algorithm in sklearn documentatio ")
        



        