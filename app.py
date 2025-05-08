import requests
import streamlit as st
from deep_translator import GoogleTranslator

@st.cache_data
def obter_resposta():
    api_url = 'https://api.api-ninjas.com/v1/advice'
    resposta = requests.get(
        api_url,
        headers={
            'X-Api-Key': st.secrets["api_key"]
            }
        )
    return resposta

def mostrar_resposta(resposta):
    if resposta.status_code == 200:
        advice = resposta.json()['advice']
        return advice
    else:
       st.error( f"Que pena agora não tem mensagem para você😓,volte depois")

def chamar_idioma():
    idioma = st.radio(
        label= 'Escolha um dos idiomas para ver sua mensagem motivacional',
        options=[
        'Português',
        'Inglês'
        ]
    )

    if idioma == 'Português':
        st.success(GoogleTranslator(
            source='en',
            target='pt'
            ).translate(mostrar_resposta(obter_resposta())))
    elif idioma == 'Inglês':
         st.success(GoogleTranslator(
            source='pt',
            target='en'
            ).translate(mostrar_resposta(obter_resposta())))     
    else:
        st.error('Foi mal ae')


st.button(
    label='Clique para outra mensagem!', 
    type='primary',
    on_click=st.cache_data.clear
    )


st.title("Mensagem incetivadora!!!")
chamar_idioma()
st.write('#####  **volte sempre que precisar de uma mensagem!!!👌** ####')



