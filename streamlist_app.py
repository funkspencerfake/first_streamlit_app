import streamlit
import pandas as pd
import requests
from urllib.error import URLError
import snowflake.connector

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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    #output it on the screen as a table
    streamlit.dataframe(back_from_function)

    

#streamlit.write('The user entered', fruit_choice)

except URLError as e:
  streamlit.error()

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json()) # just writes data to the screen

# take the json version of the response and normalize it
#fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#output it on the screen as a table
#streamlit.dataframe(fruityvice_normalized)

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor():
        my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('from streamlit')")
        return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = get_fruityvice_data(add_my_fruit)
    streamlit.text(back_from_function)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.fruit_load_list")
##my_data_row = my_cur.fetchall()
#streamlit.text("THe fruit load list contains:")
#streamlit.dataframe(my_data_row)

#fruit_add_choice = streamlit.text_input('What fruit would you like information about?', 'jackfruit')
#streamlit.text("Thanks for adding "+ fruit_add_choice) 
#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('" + fruit_add_choice + "')")
