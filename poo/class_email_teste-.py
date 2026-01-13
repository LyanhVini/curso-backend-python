# Pré-requisito: pip install requests
from abc import ABC, abstractmethod
import requests
import os
from datetime import datetime

# --- INTERFACES (Contratos) ---
class IVerificador(ABC):
    @abstractmethod
    def verificar(self) -> bool:
        """Verifica o status de um serviço e retorna True para online, False para offline."""
        pass

class IAlerta(ABC):
    @abstractmethod
    def enviar_alerta(self, mensagem: str):
        """Envia uma mensagem de alerta para um canal específico."""
        pass

# --- IMPLEMENTAÇÕES CONCRETAS ---

# Implementação do Verificador (usa GET)
class VerificadorAPI(IVerificador):
    def __init__(self, url: str):
        self.__url = url

    def verificar(self) -> bool:
        try:
            print(f"(Verificador) Checando status da URL: {self.__url}")
            response = requests.get(self.__url, timeout=5)
            if response.status_code == 200:
                print("--> Status: OK (200)")
                return True
            else:
                print(f"--> Status: ERRO ({response.status_code})")
                return False
        except requests.exceptions.RequestException as e:
            print(f"--> ERRO de Conexão: {e}")
            return False

# Implementações de Alerta (usam POST ou simulação)
class AlertaSlack(IAlerta):
    def __init__(self, webhook_url: str):
        self.__webhook_url = webhook_url

    def enviar_alerta(self, mensagem: str):
        payload = {"text": f"🚨 ALERTA URGENTE 🚨\n{mensagem}"}
        try:
            print("(Alerta) Enviando para o Slack...")
            requests.post(self.__webhook_url, json=payload, timeout=5).raise_for_status()
            print("--> Alerta enviado com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"--> ERRO ao enviar alerta para o Slack: {e}")

class AlertaEmail(IAlerta):
    def __init__(self, destinatario: str):
        self._destinatario = destinatario
        self._output_dir = "alertas_email"
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

    def enviar_alerta(self, mensagem: str):
        print(f"(Alerta) Gerando e-mail de alerta para {self._destinatario}...")
        html_content = f"<h1>ALERTA URGENTE</h1><p>{mensagem}</p>"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(self._output_dir, f"alerta_{timestamp}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"--> E-mail de alerta salvo em: '{file_path}'")

# --- CLASSE ORQUESTRADORA (Composição) ---
class Monitor:
    def __init__(self, verificador: IVerificador, alerta: IAlerta):
        self._verificador = verificador
        self._alerta = alerta

    def rodar_ciclo(self):
        print("\n" + "="*50)
        print("Iniciando novo ciclo de monitoramento...")
        if not self._verificador.verificar():
            # Se a verificação falhar, aciona o alerta!
            self._alerta.enviar_alerta("O serviço principal está offline ou retornando erro!")
        else:
            print("Serviço funcionando normalmente. Nenhuma ação necessária.")
        print("="*50)

# --- DEMONSTRAÇÃO ---
if __name__ == "__main__":
    # --- Configuração ---
    SLACK_WEBHOOK_URL = "https://webhook.site/dffcb1b1-ce77-4e9b-8efd-4a1ffa75ecc2" # SUBSTITUIR
    URL_REAL_OK = "https://api.github.com"
    URL_REAL_FALHA = "https://api.github.com/repos/isto-nao-existe"

    # --- Montando os componentes ---
    alerta_para_slack = AlertaSlack(webhook_url=SLACK_WEBHOOK_URL)
    alerta_para_email = AlertaEmail(destinatario="devops@empresa.com")
    
    verificador_servico_ok = VerificadorAPI(url=URL_REAL_OK)
    verificador_servico_falha = VerificadorAPI(url=URL_REAL_FALHA)
    
    # --- Cenário 1: Serviço OK, Alerta no Slack (NÃO deve disparar) ---
    monitor_principal = Monitor(verificador=verificador_servico_ok, alerta=alerta_para_slack)
    monitor_principal.rodar_ciclo()
    
    # --- Cenário 2: Serviço com Falha, Alerta no SLACK (DEVE DISPARAR) ---
    monitor_de_falha_slack = Monitor(verificador=verificador_servico_falha, alerta=alerta_para_slack)
    monitor_de_falha_slack.rodar_ciclo()

    # --- Cenário 3: Serviço com Falha, Alerta no Email (DEVE disparar) ---
    monitor_secundario = Monitor(verificador=verificador_servico_falha, alerta=alerta_para_email)
    monitor_secundario.rodar_ciclo()
    
    # --- Cenário 4: Serviço OK, Alerta no Email (NÃO deve disparar) ---
    monitor_secundario = Monitor(verificador=verificador_servico_falha, alerta=alerta_para_email)
    monitor_secundario.rodar_ciclo()
    
    