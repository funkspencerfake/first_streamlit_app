import streamlit
import pandas as pd
import requests

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text(':oatmeal: Omega 3 & Blueberry Oatmeal')
streamlit.text(':salad: Kale, Spinach and Rocket SMoothie')
streamlit.text(':chicken: Hard-Boiled Free-Range Egg')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('Build your own smoothie!')

fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index), ['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
streamlit.text(fruityvice_response.json()) # just writes data to the screen

# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#output it on the screen as a table
streamlit.dataframe(fruityvice_normalized)
