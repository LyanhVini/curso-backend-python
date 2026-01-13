import time
import requests

def medir_tempo(func_original):
    def wrapper():
        inicio = time.time() # pega a hora atual do sistema
        r = func_original()
        fim = time.time()
        duracao = fim - inicio
        print(f"Tempo de Duração: {duracao}")
        return r
    return wrapper

@medir_tempo
def buscar_dados():
    url = 'https://ufpa.br/'
    print("Realizando GET")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # ERRO: 400
        print(f"Status: {response.status_code}")
        print(f"Tamanho da resposta: {len(response.text)} caracteres")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        return {"status": "sucesso", "tamanho": len(response.text)}
    
    except requests.exceptions.RequestException as e:
        print(f"ERRO ao buscar dados: {e}")
        return None
    
req1 = buscar_dados()

print(req1)