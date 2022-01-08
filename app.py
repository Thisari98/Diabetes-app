# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 07:14:06 2022

@author: Thisu
"""

import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Dr.BigBot 🐘</h2>
    </div>
    
    """
    st.markdown(html_temp,unsafe_allow_html=True)


    clf = joblib.load('model_Diabetes_type')
    
    p1 = st.slider('Enter Your Age',18,100)
    
    p2 = st.number_input("Enter your Blood Sugar Fast")
    
    p3 = st.number_input("Enter your BS pp:")
    
    p4 = st.number_input("Enter your Plasma R:")
    
    p5 = st.number_input("Enter your Plasma F:")
    
    p6 = st.number_input("Enter your HbA1c:")
    
    if st.button('Predict'):
        pred = clf.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.success('Your Diabetes Type is {} '.format(pred[0]))
    
if __name__ == '__main__':
    main()
