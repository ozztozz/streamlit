import streamlit as st
import pandas as pd
mov = pd.read_csv('mov.csv')
cars = pd.read_csv('cars.csv')
hotel = pd.read_csv('hotel.csv')





st.header('Traveler List')
mov
st.header('Rental Car')
cars
st.header('Hotel')
hotel