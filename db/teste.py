import json
import datetime
from abc import ABC, abstractmethod
from typing import Dict, Any, Union

# --- Definição de Tipos (Para dar formalidade ao código) ---
Request = Dict[str, Any]
# A resposta pode ser um Dicionário (dados brutos) ou String (JSON final)
Response = Union[Dict[str, Any], str]

# ==========================================
# 1. INTERFACES (O Contrato)
# ==========================================

class HttpHandler(ABC):
    """
    Interface Component: Define o contrato para qualquer objeto
    que saiba processar uma requisição HTTP.
    """
    @abstractmethod
    def handle(self, request: Request) -> Response:
        pass

# ==========================================
# 2. COMPONENTE CONCRETO (A Regra de Negócio)
# ==========================================

class UserProfileHandler(HttpHandler):
    """
    Representa uma 'View' do Django.
    Sua única responsabilidade é buscar a lógica de negócio.
    Não sabe sobre JSON, Auth ou Logs.
    """
    def handle(self, request: Request) -> Response:
        print("   -> [Núcleo] Consultando banco de dados...")
        
        # Simulação: Lógica para pegar o ID da URL
        user_id = request.get("path", "").split("/")[-1]
        
        # Retorna dados brutos (Dicionário Python)
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
    Classe base para todos os Decorators.
    Mantém a referência para o 'próximo' item da cadeia (wrappee).
    """
    def __init__(self, next_handler: HttpHandler):
        self._next_handler = next_handler

    def handle(self, request: Request) -> Response:
        # O comportamento padrão é repassar para o próximo
        return self._next_handler.handle(request)

# ==========================================
# 4. DECORATORS CONCRETOS (Infraestrutura)
# ==========================================

class AuthenticationMiddleware(Middleware):
    """
    Responsabilidade: Segurança (Protection Proxy/Decorator).
    Verifica se o token existe antes de deixar passar.
    """
    def handle(self, request: Request) -> Response:
        print("[Auth] Verificando credenciais...")
        
        headers = request.get("headers", {})
        token = headers.get("Authorization")
        
        # Lógica de Bloqueio (Short-circuit)
        if token != "Bearer SENHA_SECRETA":
            print("[Auth] ⛔ Bloqueado! Token inválido ou ausente.")
            # Retorna erro imediatamente, NÃO chama o super().handle()
            return {"status": 403, "error": "Forbidden: Invalid Token"}
        
        print("[Auth] ✅ Token válido. Passando adiante.")
        return super().handle(request)


class LoggingMiddleware(Middleware):
    """
    Responsabilidade: Auditoria.
    Registra o tempo e o status da requisição.
    """
    def handle(self, request: Request) -> Response:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        path = request.get("path", "/")
        
        print(f"[Log @ {timestamp}] ➡️ Requisição iniciada para: {path}")
        
        # Chama a cadeia e captura o resultado
        response = super().handle(request)
        
        # Tenta ler o status (pode ser dict ou str se já virou json)
        status = "OK"
        if isinstance(response, dict):
            status = response.get("status")
            
        print(f"[Log @ {timestamp}] ⬅️ Requisição finalizada. Status: {status}")
        return response


class JSONResponseMiddleware(Middleware):
    """
    Responsabilidade: Transformação de Dados.
    Converte o dicionário Python em String JSON para a web.
    """
    def handle(self, request: Request) -> Response:
        # 1. Executa toda a cadeia interna para pegar os dados brutos
        raw_response = super().handle(request)
        
        # 2. Transforma a resposta (Pós-processamento)
        if isinstance(raw_response, dict):
            print("[JSON] 🔄 Serializando dicionário para formato JSON...")
            return json.dumps(raw_response, indent=4, ensure_ascii=False)
        
        return raw_response

# ==========================================
# 5. CÓDIGO CLIENTE (Simulação do Servidor)
# ==========================================

if __name__ == "__main__":
    print("--- INICIALIZANDO SERVIDOR ---")
    
    # 1. Configuração da Rota (O "Núcleo" da cebola)
    core_handler = UserProfileHandler()
    
    # 2. Construção da Pilha de Middlewares (Decorators)
    # A leitura do código é de fora para dentro, a execução depende da lógica.
    # Pipeline Lógico: JSON -> Log -> Auth -> Core
    
    application = JSONResponseMiddleware(
                    LoggingMiddleware(
                        AuthenticationMiddleware(core_handler)
                    )
                  )
    
    print("Servidor pronto.\n")

    # --- CASO 1: Requisição Falha (Sem Token) ---
    print(">>> Cenário 1: Hacker tentando acessar sem token")
    request_hacker = {
        "path": "/api/users/666",
        "headers": {"User-Agent": "Mozilla/5.0"}
    }
    
    response = application.handle(request_hacker)
    print(f"\nRESPOSTA HTTP (Body):\n{response}")

    print("\n" + "="*50 + "\n")

    # --- CASO 2: Requisição Sucesso (Com Token) ---
    print(">>> Cenário 2: Admin acessando com token correto")
    request_admin = {
        "path": "/api/users/10",
        "headers": {
            "Authorization": "Bearer SENHA_SECRETA",
            "User-Agent": "Postman"
        }
    }
    
    response = application.handle(request_admin)
    print(f"\nRESPOSTA HTTP (Body):\n{response}")