import functools

context_user = {"usuario_logado": None}

def login_requirido(func_original):
    @functools.wraps(func_original)
    def wrapper(*args, **kwargs):
        # Verificação
        if context_user["usuario_logado"] is None:
            print("ACESSO NEGADO")
            # Redirecionar para login
            return
        else:
            print(f"Acesso permitido para {func_original.__name__}")
            return func_original(*args, **kwargs)
    return wrapper
        
@login_requirido
def painel_usuario(nome_usuario):
    print(f"Bem-vindo ao seu painel: {nome_usuario}")
    return "Página do Painel"

def pagina_inicial():
    print("Bem-vindo a página pública!")
    
pagina_inicial()
r_painel1 = painel_usuario("Falha")
print(r_painel1)

#simulando login
context_user["usuario_logado"] = "Maria"
r_painel2 = painel_usuario("Maria")
print(r_painel2)


