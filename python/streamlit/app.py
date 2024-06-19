import streamlit as st
import requests
import json


base_url = "https://api.chucknorris.io/jokes/"


categorias = requests.get(f"{base_url}/categories").content.decode("utf-8")

categorias = json.loads(categorias)
print(categorias)





st.title("isso é um titulo")

options = st.multiselect(
    label = 'Quais sao as categorias que voce quer?:',
    options = categorias,
    default = [categorias[0]]
)

st.write("voce escolheu: ", options)

for category in options:
    
    response=json.loads(requests.get(f"{base_url}/random?category={category}").content.decode('utf-8'))
    
    st.header(f"frase da categoria {category}:")
    st.write(response.get('value'))
    
    