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
         st.write('')
def chamar_idioma():
    try:
        idioma = st.radio(
            label= 'Escolha um dos idiomas para ver sua mensagem motivacional',
            options=[
                'Português',
                'Inglês',
                'Espanhol'
            ]
        )

        if idioma == 'Português':
            st.success(GoogleTranslator(
                source='en',
                target='pt'
            ).translate(mostrar_resposta(obter_resposta())))
        elif idioma == 'Espanhol':
            st.success(GoogleTranslator(
                source='en',
                target='es'
            ).translate(mostrar_resposta(obter_resposta())))
        else:
            st.success(mostrar_resposta(obter_resposta()))      
    except Exception:
        st.error('Foi mal mas nao consigo gerar sua mensagem')


st.button(
    label='Clique para outra mensagem!', 
    type='primary',
    on_click=st.cache_data.clear
    )


st.title("Mensagem incetivadora!!!")
chamar_idioma()
st.write('#####  **Volte sempre que precisar de uma mensagem!!!👌** ####')
