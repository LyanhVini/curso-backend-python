from abc import ABC, abstractmethod
import requests # fazer requisição
import datetime # pra ver hora do sistema

# Interfaces - Classes Abstratas
class IVerificador(ABC):
    @abstractmethod
    def verificar(self) -> bool:
        pass

class IAlerta(ABC):
    @abstractmethod
    def enviar_alerta(self, mensagem: str):
        pass

# Classes Concretas

class VerificadorAPI(IVerificador):
    def __init__(self, url: str):
        self.__url = url # privado
    
    def verificar(self) -> bool:
        try:
            response = requests.get(self.__url, timeout=5)
            if response.status_code == 200:
                print("--> Status: OK (200)")
                return True
            else:
                print("--> Status: ERRO")
        except requests.exceptions.RequestException as e:
            print(f"--> ERRO DE CONEXÃO: {e}")
            return False
        
class AlertaSlack(IAlerta):
    def __init__(self, webhook_url: str):
        self.__webhook_url = webhook_url
        
    def enviar_alerta(self, mensagem: str):
        
        payload = {"text:": f"ALERTA URGENTE TESTE \n{mensagem}"}
        
        try:
            print("(ALERTA) Enviando para o slack...")
            requests.post(self.__webhook_url, json=payload, timeout=5).raise_for_status()
            print("Alerta enviado com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"--> ERRO ao enviar alerta ao Slack: {e}")

class AlertaEmail(IAlerta):
    def __init__(self, destinatario: str):
        self._destinatario = destinatario
    
    def enviar_alerta(self, mensagem: str):
        print(f"(Alerta) Gerando e-mail para {self._destinatario}")

class Monitor:
    def __init__(self, verificador: IVerificador, alerta: IAlerta):
        self._verificador = verificador
        self._alerta = alerta
        
    def rodar_ciclo(self):
        print("Iniciando novo ciclo...")
        if self._verificador.verificar():
            print("Serviço funcionando normalmente.")
        else:
            self._alerta.enviar_alerta("O serviço está offilen ou retornando erro.")
            
url_webhook = 'https://webhook.site/dffcb1b1-ce77-4e9b-8efd-4a1ffa75ecc2'
url_real = 'https://ufpa.br/'
url_fake = 'https://urlfakke.br/'

alerta_para_slack = AlertaSlack(url_webhook)
alerta_para_email = AlertaEmail("devops@gmail.com")

verificador_ok = VerificadorAPI(url=url_real)
verificador_falha = VerificadorAPI(url=url_fake)

# 1 cenário: serviço OK 
monitor_principal = Monitor(verificador_ok, 
                            alerta_para_slack)
monitor_principal.rodar_ciclo()

# 2 cenário: serviço FALHA 
monitor_secundario = Monitor(verificador_falha, 
                            alerta_para_slack)
monitor_secundario.rodar_ciclo()