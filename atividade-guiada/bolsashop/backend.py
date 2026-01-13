import sqlite3
from typing import Dict, Any
from abc import ABC, abstractmethod
# 1. Strategy Pattern (lógica de negócio)
class PagamentoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor_bruto: float) -> float:
        pass
class PixStrategy(PagamentoStrategy):
    def calcular(self, valor_bruto: float) -> float:
        return valor_bruto * 0.90 # aplica 10% desconto
class CartaoStrategy(PagamentoStrategy):
    def calcular(self, valor_bruto: float) -> float:
        return valor_bruto * 1.05 # aplico 5 % de juros do valor original
# 2. Database Services (código para sqlite):
class PedidoService:
    def __init__(self, db_name='ecommerce_db'):
        self.db_name = db_name
        
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    
    def buscar_valor_pedido(self, pedido_id: int) -> float:
        conn = self.get_connection()
        cursor = conn.cursor()
        # Mysql -> %s  // sqlite -> ?
        sql = "SELECT valor_bruto FROM pedidos WHERE id = ? AND status = 'PENDENTE'"
        cursor.execute(sql, (pedido_id,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if resultado:
            return float(resultado[0])
        return None
    
    def processar_pagamento_db(self, pedido_id: int, metodo: str, valor_final: float):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # 1. Registrar o Pagamento
            sql_insert = 'INSERT INTO pagamentos(pedido_id, metodo, valor_final) VALUES (?, ?, ?)'
            cursor.execute(sql_insert, (pedido_id, metodo, valor_final))
            
            # 2. Atualizar o status do Pedido
            sql_update = 'UPDATE pedidos SET status = "PAGO" WHERE id = ?'
            cursor.execute(sql_update, (pedido_id,))
            
            # 3. Realizar o commit
            conn.commit()
            print("[DB] Transação realizada com sucesso")
            
        except Exception as e:
            conn.rollback()
            print(f"[DB] Erro de transação: {e}")
        finally:
            cursor.close()
            conn.close()
# 3. Controller (orquestrador):
class CheckoutController:
    def __init__(self):
        self.strategies = {
            "PIX": PixStrategy(),
            "CARTAO": CartaoStrategy()
        }
        self.service = PedidoService()
    
    def handle_request(self, request: Dict[str, Any]):
        # 1. Processar a Requisição
        # request: {"pedido_id": X, "metodo": Y}
        # resgatar o métood de pagamento
        pedido_id = request.get('pedido_id')
        metodo = request.get('metodo')
        
        print(f"------ Processando Pedido #{pedido_id}-----")
        # 2. Validar os dados
        valor_bruto = self.service.buscar_valor_pedido(pedido_id)
        if valor_bruto is None:
            return {"status": 404, "error": "Pedido não encontrado ou já pago"}
        # 3. Aplicar a estratégias de pagamento
        if metodo not in self.strategies:
            return {"status": 404, "error": "Método de pagamento inválido"}
        
        strategy = self.strategies[metodo]
        valor_final = strategy.calcular(valor_bruto)
        
        print(f"Valor original: R$ {valor_bruto:.2f}")
        print(f"Valor Final: R$ {valor_final:.2f}")
        # 4. Garantir a persistencia do DB
        self.service.processar_pagamento_db(pedido_id, metodo, valor_final)
        # 5. Retorno o JSON
        return {"status": 200, "msg": "Pagamento Aprovado"}
        
# 4. Simulação:
if __name__ == "__main__":
    
    controller = CheckoutController()
    
    # Cenário 1: Pagamento do pedido 1 com PIX
    req1 = {"pedido_id": 1, "metodo": "PIX"}
    print(controller.handle_request(req1))
    # Cenário 2: Pagamento do pedido 2 com Cartão
    req2 = {"pedido_id": 2, "metodo": "CARTAO"}
    print(controller.handle_request(req2))
    # Cenário 3: Pagamento do pedido 1 com PIX (erro)
    print(controller.handle_request(req1))