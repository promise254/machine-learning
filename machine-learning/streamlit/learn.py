import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv('data/dada.csv')
print(data)
x=data.drop(columns=['genre'])
y=data['genre']

#g=data.drop(columns=['age'])
#age=data['age']
#new=data['doubleage']=data['age']*2

module=DecisionTreeClassifier()
module.fit(x, y)
prediction=module.predict([ [27,1] ])
print(prediction)


st.write(prediction)