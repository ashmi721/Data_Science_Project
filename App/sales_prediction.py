import pickle
import streamlit as st

with open('pickle file/modelLinear.pickle','rb') as file:
    model = pickle.load(file)
    
tv = st.text_input('TV adds')   
if st.button('Submit'):
    y_pred = model.predict([[int(tv)]])
    st.write(f'Your Sales must be around {y_pred[0]}') 