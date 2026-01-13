class CDs:
    def __init__(self, titulo:str, ano:int, ehDuplo=False, ehColetania=False):
        self.titulo = titulo
        self.ano = ano
        self.ehDuplo = ehDuplo
        self.ehColetania = ehColetania
        self.musicas = []
        self.musicos = []
        
    def cadastrar(self):
        print(f"CD {self.titulo} cadastrado com sucesso!")
        
    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        musica.cds.append(self)
    
    def adicionar_musico(self, musico):
        self.musicos.append(musico)
        musico.cds.append(self)
        
    def listarCDS_Musica(musica, lista_cds):
        cds_da_musica = []
        for cd in lista_cds:
            if musica in cd.musicas:
                cds_da_musica.append(cd)
        return cds_da_musica
    
    def listarCDS_Musico(musico, lista_cds):
        cds_da_musico = []
        for cd in lista_cds:
            if musico in cd.musicos:
                cds_da_musico.append(cd)
        return cds_da_musico
    
    def listar_musicas(self):
        print(self.musicas)
    
    def listar_musicos(self):
        print(self.musicos)  
    
class Musico:
    def __init__(self, nome:str, ehSolo=True):
        
        self.nome = nome
        self.ehSolo = ehSolo
        self.cds = []
        
    def cadastrar(self):
        print(f"Músico {self.nome} cadastrado com sucesso!")
        
class Musica:
    def __init__(self, nome:str, tempoFaixa:float):
        self.nome = nome
        self.tempoFaixa = tempoFaixa
        self.cds = []
        
    def cadastrar(self):
        print(f"Música {self.nome} cadastrada com sucesso!")
    

# Criando Músicos
roberto_carlos = Musico("Roberto Carlos", True) 
tim_maia = Musico("Tim Maia", True)
renato_russo = Musico("Renato Russo", True)
detonautas = Musico("Detonautas", False)
#print(roberto_carlos.nome)
#print(type(roberto_carlos))

# Criando Músicas:

musica1 = Musica("Música 1", 3.40)
musica2 = Musica("Música 2", 2.57)
musica3 = Musica("Música 3", 3.15)

# Criando CDS

cd1 = CDs("As melhores do Roberto Carlos", 1995, True)
cd2 = CDs("Tim Maia - Acústico", 1997, False)

# Configurando Relações (Música -> CDS)
cd1.adicionar_musica(musica1)
cd2.adicionar_musica(musica2)
cd1.adicionar_musico(roberto_carlos)
cd1.adicionar_musico(tim_maia)
cd1.adicionar_musico(renato_russo)
cd2.adicionar_musico(detonautas)
cd2.adicionar_musico(tim_maia)
cd2.adicionar_musica(musica3)

print("\nListagem:\n")
cd1.listar_musicas()
cd2.listar_musicas()
cd1.listar_musicos()
cd2.listar_musicos()

todos_cds = [cd1, cd2] # coletânia

#CADASTRANDO:

roberto_carlos.cadastrar()
musica1.cadastrar()
cd1.cadastrar()

print("CDS do Roberto Carlos")
cds_roberto = CDs.listarCDS_Musico(roberto_carlos, todos_cds)
for cd in cds_roberto:
    print(f"- {cd}")

print("CDS de uma música")
cds_musica = CDs.listarCDS_Musica(musica1, todos_cds)
for cd in cds_musica:
    print(f"- {cd}")
    
print(roberto_carlos)
print(musica1)
print(cd1)

print("\nCD1: \n")
print(f"Músicas do CD1: {[musica.nome for musica in cd1.musicas]}")
print(f"Músicos do CD1: {[musico.nome for musico in cd1.musicos]}")

print("\nCD2: \n")
print(f"Músicas do CD2: {[musica.nome for musica in cd2.musicas]}")
print(f"Músicos do CD2: {[musico.nome for musico in cd2.musicos]}")







