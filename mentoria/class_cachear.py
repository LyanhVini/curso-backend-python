import functools
import time

_cache_simples = {} # [chave]:valor

def cachear(func_origin):
    @functools.wraps(func_origin)
    def wrapper(*args, **kwargs):
        
        chave_cache = (func_origin.__name__, args, tuple(sorted(kwargs.items())))

        if chave_cache in _cache_simples:
            print(f"Cache HIT para {chave_cache}")
            return _cache_simples[chave_cache]
        else:
            print(f"Cache MISS para {chave_cache}")
            resultado = func_origin(*args, **kwargs)
            _cache_simples[chave_cache] = resultado
            return resultado
    return wrapper

@cachear
def consulta_db(query: str):
    print(f"Executando consulta no DB: {query}")
    time.sleep(2) # tempo de execução
    return f"Resultado para {query}"

# SIMULAÇÕES
res1 = consulta_db("SELECT * from usuarios")
print("Resultado 1: ", res1)

res2 = consulta_db("SELECT * from usuarios")
print("Resultado 2: ", res2)

