import functools
import time
from dataclasses import dataclass
import requests
from requests.exceptions import RequestException
from typing import Dict, Any, Callable

@dataclass(frozen=True) # __init__(id, nome_usuario, email, cidade), __eq__, __str__, __repr__
class ApiUser:
    id: int
    nome_usuario: str
    email: str
    cidade: str
    
    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'ApiUser':
        """Trata os dados JSON recebido para instanciar corretamente a classe."""
        try:
            return cls(
                id = data['id'],
                nome_usuario = data['username'],
                email = data['email'],
                cidade = data['address']['city']
            )
        except (KeyError, TypeError) as e:
            raise ValueError(f"Formato de JSON inesperado: {e}")

def retry_on_file(tries: int, delay_sec: int) -> Callable: 
    def decorador(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(tries):
                try:
                    return func(*args, *kwargs)
                except RequestException as e:
                    last_exception = e
                    print("[RETRY] Falha na chamada {e.__class__.__name__}. Tentando novamente em {delay_sec}...")
                    time.sleep(delay_sec)
            raise last_exception
        return wrapper
    return decorador

api_url = 'https://jsonplaceholder.typicode.com/users'

@functools.cache
@retry_on_file(tries=3, delay_sec=2)
def fetch_user_by_id(user_id: int) -> ApiUser:
    """Busca de um usuário da API externa"""
    print(f"[API] Buscando dados na rede para {user_id}")
    
    url = f"{api_url}/{user_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return ApiUser.from_json(response.json())
    
if __name__ == "__main__":
    
    print("Chamada com Sucesso (lenta)")
    start = time.perf_counter()
    user1 = fetch_user_by_id(1)
    print(f"Resultado: {user1}")
    print(f"Tempo: {time.perf_counter() - start:.2f}")
    
    print("Chamada com Sucesso (rápida)")
    start = time.perf_counter()
    user2 = fetch_user_by_id(1)
    print(f"Resultado: {user2}")
    print(f"Tempo: {time.perf_counter() - start:.2f}")
    
    print("Chamada com Sucesso (rápida)")
    start = time.perf_counter()
    user3 = fetch_user_by_id(5)
    print(f"Resultado: {user3}")
    print(f"Tempo: {time.perf_counter() - start:.2f}")
    
    print(user1 == user2) # true
    print(user1 == user3) # false
    
    
    
    