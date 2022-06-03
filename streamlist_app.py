import streamlit
import pandas as pd

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text(':oatmeal: Omega 3 & Blueberry Oatmeal')
streamlit.text(':salad: Kale, Spinach and Rocket SMoothie')
streamlit.text(':chicken: Hard-Boiled Free-Range Egg')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list.set_index('Fruit', inplace=True)
streamlit.header('Build your own smoothie!')

streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index), ['Avocado','Strawberry'])

streamlit.dataframe(my_fruit_list)
