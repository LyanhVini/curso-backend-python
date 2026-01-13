class InscricaoCurso:
    
    def __init__(self, aluno: str, curso: str):
        
        self.aluno = aluno
        self.curso = curso
        self.status = 'Pendente' #RF01
    
    def confirmar_matricula(self):
        if self.status == 'Pendente':
            self.status = 'Confirmada'
            print("Matricula confirmada!") 
        else:
            print("A matricula de {self.aluno} não pode ser confirmada" +
                  "pois o seu status atual é {self.status}") 
    
    def cancelar_matricula(self):
        if self.status == 'Cancelado': # RF03
            print("Matrícula já está cancelada")
        else:
            self.status = 'Cancelado'
            print("Matrícula Cancelada") 
            
    def consultar_status(self):
        print(f"[CONSULTA] Status da inscrição de {self.aluno}: {self.status}") 
        
inscricao_joao = InscricaoCurso("João", "Backend Python")
inscricao_joao.consultar_status()
inscricao_joao.confirmar_matricula()
inscricao_joao.consultar_status()
inscricao_joao.cancelar_matricula()
inscricao_joao.consultar_status()