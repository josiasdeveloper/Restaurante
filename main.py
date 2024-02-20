from fastapi import FastAPI, Query
import requests as rq

app = FastAPI()

@app.get('/api/hello')
def helloWorld():
    return {'Message' : 'Hello World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None) ):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = rq.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                'Item': item['Item'],
                'Price': item['price'],
                'Description': item['description']
            })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}        
        
    
