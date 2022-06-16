import requests
import pandas as pd
import collections
import sys

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'
df_bronze = requests.get(url)
tx = df_bronze.text
tx = tx.replace('\\r\\n', '')
tx = tx.replace('{\r\n "html": ', '')
tx = tx.replace('"\r\n}', '')
df_prata = pd.read_html(tx)
df_ouro = df_prata[0]
df_ouro[df_ouro['Bola1'].notnull() == True]