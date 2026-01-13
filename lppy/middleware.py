import json
import datetime
from abc import ABC, abstractmethod
from typing import Dict, Any, Union

# --- Definição de Tipos (Type Hinting) ---
# Usamos Type Hinting para tornar o código autodocumentável e robusto.
# Request: Um dicionário contendo metadados (headers, path, body).
Request = Dict[str, Any]
# Response: Pode ser um dict (dados internos) ou str (JSON final para o cliente).
Response = Union[Dict[str, Any], str]

# ==========================================
# 1. INTERFACES (O Contrato / Component)
# ==========================================

class HttpHandler(ABC):
    """
    Define a interface comum. Tanto a 'View' (rota) quanto os 'Middlewares'
    devem herdar daqui. Isso garante que todos tenham o método 'handle'.
    """
    @abstractmethod
    def handle(self, request: Request) -> Response:
        pass

# ==========================================
# 2. COMPONENTE CONCRETO (A Regra de Negócio)
# ==========================================

class UserProfileHandler(HttpHandler):
    """
    Equivale a uma 'View' no Django. É o NÚCLEO da cebola.
    Sua única função é processar a lógica de negócio e devolver dados.
    """
    def handle(self, request: Request) -> Response:
        print("   -> [Núcleo] Consultando banco de dados...")
        
        # Lógica simulada: extrai o ID do final da URL
        user_id = request.get("path", "").split("/")[-1]
        
        # Retorna um Dicionário puro (ainda não é JSON).
        # Isso mantém o desacoplamento: a View não sabe como os dados serão serializados.
        return {
            "status": 200,
            "data": {
                "id": user_id,
                "name": "Maria Silva",
                "role": "Backend Student",
                "active": True
            }
        }

# ==========================================
# 3. DECORATOR BASE (A Camada de Middleware)
# ==========================================

class Middleware(HttpHandler):
    """
    Classe base que implementa a 'colagem' do padrão Decorator.
    Ela recebe o 'próximo' item da fila e o armazena.
    """
    def __init__(self, next_handler: HttpHandler):
        # Armazena a referência para o objeto que será envolvido (wrappee).
        self._next_handler = next_handler

    def handle(self, request: Request) -> Response:
        # Delegação: O comportamento padrão é simplesmente passar a batata quente
        # para o próximo handler da lista.
        return self._next_handler.handle(request)

# ==========================================
# 4. DECORATORS CONCRETOS (Infraestrutura)
# ==========================================

class AuthenticationMiddleware(Middleware):
    """
    Padrão: Protection Proxy / Decorator.
    Lógica aplicada ANTES da execução do núcleo.
    """
    def handle(self, request: Request) -> Response:
        print("[Auth] Verificando credenciais...")
        
        headers = request.get("headers", {})
        token = headers.get("Authorization")
        
        # --- Short-Circuit (Curto-circuito) ---
        # Se a validação falhar, retornamos a resposta aqui mesmo.
        # O 'super().handle()' NÃO é chamado, impedindo o acesso ao núcleo.
        if token != "Bearer SENHA_SECRETA":
            print("[Auth] ⛔ Bloqueado! Token inválido ou ausente.")
            return {"status": 403, "error": "Forbidden: Invalid Token"}
        
        print("[Auth] ✅ Token válido. Passando adiante.")
        # Se passou, chama o próximo da fila.
        return super().handle(request)


class LoggingMiddleware(Middleware):
    """
    Padrão: Decorator com Side-Effect (Efeito Colateral).
    Executa lógica ANTES e DEPOIS do núcleo, mas não altera os dados.
    """
    def handle(self, request: Request) -> Response:
        # 1. Antes da execução (Pre-processing)
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        path = request.get("path", "/")
        print(f"[Log @ {timestamp}] ➡️ Requisição iniciada para: {path}")
        
        # 2. Chama a cadeia e aguarda o retorno (vai até o núcleo e volta)
        response = super().handle(request)
        
        # 3. Depois da execução (Post-processing)
        # Verifica o status sem alterar a resposta original
        status = "OK"
        if isinstance(response, dict):
            status = response.get("status")
            
        print(f"[Log @ {timestamp}] ⬅️ Requisição finalizada. Status: {status}")
        return response


class JSONResponseMiddleware(Middleware):
    """
    Padrão: Decorator de Transformação.
    Altera o TIPO do dado retornado (de Dict para String JSON).
    """
    def handle(self, request: Request) -> Response:
        # 1. Executa toda a cadeia primeiro para obter os dados brutos (dict)
        raw_response = super().handle(request)
        
        # 2. Transforma o resultado final (Pós-processamento)
        if isinstance(raw_response, dict):
            print("[JSON] 🔄 Serializando dicionário para formato JSON...")
            # Transforma Dict Python -> String JSON
            return json.dumps(raw_response, indent=4, ensure_ascii=False)
        
        return raw_response

# ==========================================
# 5. CÓDIGO CLIENTE (Configuração e Execução)
# ==========================================

if __name__ == "__main__":
    print("--- INICIALIZANDO SERVIDOR ---")
    
    # 1. Instancia o Núcleo (A View)
    core_handler = UserProfileHandler()
    
    # 2. Monta a 'Cebola' (Pipeline de Execução)
    # A ordem de instanciação é de DENTRO para FORA.
    # Mas a execução da requisição é de FORA para DENTRO.
    # Fluxo: JSON -> Log -> Auth -> Core -> (volta) -> Auth -> Log -> JSON
    
    application = JSONResponseMiddleware(          # Camada Externa
                    LoggingMiddleware(             # Camada do Meio
                        AuthenticationMiddleware(  # Camada Interna
                            core_handler           # Núcleo
                        )
                    )
                  )
    
    print("Servidor pronto.\n")

    # --- Simulação ---
    print(">>> Cenário 2: Admin acessando com token correto")
    request_admin = {
        "path": "/api/users/10",
        "headers": {
            "Authorization": "Bearer SENHA_SECRETA",
            "User-Agent": "Postman"
        }
    }
    
    # O cliente chama apenas o objeto mais externo (application)
    # Ele não sabe que existem camadas internas.
    response = application.handle(request_admin)
    print(f"\nRESPOSTA HTTP (Body):\n{response}")