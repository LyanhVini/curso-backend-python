from  abc import ABC, abstractmethod
import bcrypt # criptográfico
from enum import Enum # gerenciar status
from datetime import datetime, timezone

# StatusUsuario: contem os variáveis de status de cada usuário
class StatusUsuario(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"
    BANIDO = "Banido"
    
# Comentario: simular um comentário do sistema
class Comentario:
    def __init__(self, autor: str, texto: str):
        self.autor = autor
        self.texto = texto
        self.visivel = True  
        
# CLASSES ABSTRATAS E CONCRETAS
class Usuario(ABC):
    def __init__(self, username: str, email: str, senha_hash: bytes):
        self.username = username
        self.email = email
        self.__senha_hash = senha_hash
        self._status = StatusUsuario.ATIVO
        self.data_criacao = datetime.now(timezone.utc)
    
    def verificador_senha(self, senha_texto:str):
        return bcrypt.checkpw(senha_texto.encode('utf-8'), self.__senha_hash)
    
    def get_status(self):
        return self._status
    
    def _set_status(self, novo_status: StatusUsuario):
        self._status = novo_status
        
    @abstractmethod
    def tem_permissao(self, acao: str) -> bool:
        pass

class UsuarioComum(Usuario):
    
    def tem_permissao(self, acao:str) -> bool:
        return acao == "visualizar_post"
    
class Moderador(UsuarioComum):
    
    def deletar_comentario(self, comentario: Comentario):
        if self.tem_permissao("deletar_comentario"):
            comentario.visivel = False
            print(f"[{self.username} - Moderador] Comentário de {comentario.autor} foi ocultado")
        else:
            print(f"[{self.username}] Acesso negato para deletar esse comentário.")
            
    def tem_permissao(self, acao:str):
        
        if acao == "deletar_comentario":
            return True

        return super().tem_permissao(acao)

class Admin(Moderador):
    
    def tem_permissao(self, acao:str) -> bool:
        return True
    
    def banir_usuario(self, usuario_alvo: Usuario):
        
        if self.tem_permissao("banir_usuario"):
            usuario_alvo._set_status(StatusUsuario.BANIDO)
            print(f"[{self.username} - Admin] Usuário {usuario_alvo.username} foi BANIDO")
        else:
            print(f"[{self.username}] Acesso negado para banir esse usuário.")            
            
class GerenciadorDeUsuarios:
    
    def __init__(self):
        
        self.__usuarios = {}
        self.__sessao_ativa = None
        
    def registrar(self, username: str, email: str, senha: str, nivel: str = "comum"):
        
        if username in self.__usuarios:
            print(f"ERRO: Usuário {username} já existe")
            return
        
        # CRIPTOGRAFIA
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        
        mapa_de_niveis = {
            "comum": UsuarioComum,
            "moderador": Moderador,
            "admin": Admin
        }
        
        classe_usuario = mapa_de_niveis.get(nivel)
        
        if classe_usuario:
            novo_usuario = classe_usuario(username, email, senha_hash)
            self.__usuarios[username] = novo_usuario
            print(f"Usuário {username} registrado com sucesso!")
        else:
            print(f"ERRO: Nível {nivel} desconhecido.")
            
    def buscar_usuario(self, username: str) -> Usuario | None: 
        return self.__usuarios.get(username)
    
    def login(self, username: str, senha: str):
        
        if self.__sessao_ativa:
            print("ERRO: Já existe uma sessao ativa para esse usuário.")
        
        usuario = self.buscar_usuario(username)
        if usuario and usuario.verificador_senha(senha):
            if usuario.get_status() == StatusUsuario.ATIVO:
                self.__sessao_ativa = usuario
                print(f"Login bem-sucedido!")
                
            else:
                print("Falha no Login")
        else:
            print(f"Falha no login para {username}. Credenciais Inválidas")
             
    
    def logout(self):
        if self.__sessao_ativa:
            print(f"Sessão de {self.__sessao_ativa.username} encerrada")
            self.__sessao_ativa = None
        else:
            print("Nenhuma sessão ativa para encerrar")
            
    def get_usuario_logado(self) -> Usuario | None:
        
        return self.__sessao_ativa
    
    
##############################################4

sistema = GerenciadorDeUsuarios()

sistema.registrar("joao", "joao@gmail.com", "senha123", "comum")
sistema.registrar("ana", "ana@gmail.com", "senha456", "moderador") 
sistema.registrar("chefe_adm", "adm@gmail.com", "senha789", "admin")   

# TESTE COM USUARIO COMUM E PERMISSÂO
#sistema.login("joao", "senha123")

# Login com moderador e teste de ação
sistema.login("ana", "senha456")
moderadora_logada = sistema.get_usuario_logado()
if moderadora_logada and isinstance(moderadora_logada, Moderador):
    comentario = Comentario(autor="joao", texto="Primeiro a comentar!")
    moderadora_logada.deletar_comentario(comentario)
    print(f"Visibilidade do comentário: {comentario.visivel}")
sistema.logout()
        
# ADMIN
sistema.login("chefe_adm", "senha789")

admin_logado = sistema.get_usuario_logado()

usuario_a_ser_banido = sistema.buscar_usuario("joao")

if admin_logado and isinstance(admin_logado, Admin) and usuario_a_ser_banido:
    admin_logado.banir_usuario(usuario_a_ser_banido)
    print(f"Status de {usuario_a_ser_banido.username}: {usuario_a_ser_banido.get_status().value}")

sistema.logout()