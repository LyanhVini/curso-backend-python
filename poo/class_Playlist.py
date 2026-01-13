class Musica:
    def __init__(self, titulo, artista, duracao_seg):
        self.titulo = titulo
        self.artista = artista
        self.duracao_seg = duracao_seg

    def __repr__(self):
        """
        Representação técnica para o desenvolvedor.
        Retorna uma string que poderia, idealmente, recriar o objeto.
        """
        return f"Musica(titulo='{self.titulo}', artista='{self.artista}')"
    
    def __str__(self):
        """Representação amigável."""
        return f"{self.titulo} - {self.artista}"


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self._musicas = []  

    def adicionar_musica(self, musica: Musica):
        """Método auxiliar para adicionar músicas à lista."""
        self._musicas.append(musica)
        print(f"Música '{musica.titulo}' adicionada à playlist '{self.nome}'.")

    # --- Requisito 1: Representação Amigável ---
    def __str__(self):
        """
        Chamado por: print(playlist)
        Retorna uma string amigável para o usuário final.
        """
        total_musicas = len(self._musicas)
        return f"Playlist '{self.nome}' ({total_musicas} músicas)"

    # --- Requisito 2: Representação Técnica ---
    def __repr__(self):
        """
        Chamado por: repr(playlist) ou ao imprimir uma lista de playlists.
        Retorna uma string técnica para o desenvolvedor.
        """
        return f"Playlist(nome='{self.nome}')"

    # --- Requisito 3: Comportamento de Tamanho ---
    def __len__(self):
        """
        Chamado por: len(playlist)
        Delega a lógica de "tamanho" para a lista interna.
        """
        return len(self._musicas)

    # --- Requisito 4: Comportamento de Acesso por Índice ---
    def __getitem__(self, index):
        """
        Chamado por: playlist[index]
        Delega o acesso por índice para a lista interna.
        """
        return self._musicas[index]

    # --- Requisito 5: Comportamento de Adição (Soma) ---
    def __add__(self, other):
        """
        Chamado por: playlist1 + playlist2
        Deve retornar um *novo* objeto Playlist.
        """
        if not isinstance(other, Playlist):
            return NotImplemented  # Indica que não sabe somar com esse tipo

        # Cria uma nova playlist para o mix
        novo_nome = f"Mix: {self.nome} + {other.nome}"
        nova_playlist = Playlist(novo_nome)

        # Adiciona as músicas da primeira playlist
        for musica in self:  # Podemos iterar em 'self' por causa do __getitem__ e __len__
            nova_playlist._musicas.append(musica)
        
        # Adiciona as músicas da segunda playlist
        for musica in other:
            nova_playlist._musicas.append(musica)
            
        return nova_playlist

if __name__ == "__main__":
    # 1. Criar Músicas
    m1 = Musica("Bohemian Rhapsody", "Queen", 354)
    m2 = Musica("Stairway to Heaven", "Led Zeppelin", 482)
    m3 = Musica("Shape of You", "Ed Sheeran", 233)
    m4 = Musica("Blinding Lights", "The Weeknd", 200)

    # 2. Criar Playlists e adicionar músicas
    playlist_rock = Playlist("Rock Clássico")
    playlist_rock.adicionar_musica(m1)
    playlist_rock.adicionar_musica(m2)

    print("-" * 30)
    playlist_pop = Playlist("Pop Hits")
    playlist_pop.adicionar_musica(m3)
    playlist_pop.adicionar_musica(m4)
    print("-" * 30)

    # 3. Testar os Requisitos
    print("\n--- Testando __str__ (print) ---")
    print(playlist_rock)
    print(playlist_pop)

    print("\n--- Testando __repr__ (representação técnica) ---")
    print(repr(playlist_rock))
    print(f"Playlists em uma lista: {[playlist_rock, playlist_pop]}")

    print("\n--- Testando __len__ (tamanho) ---")
    print(f"Músicas na playlist de Rock: {len(playlist_rock)}")
    print(f"Músicas na playlist de Pop: {len(playlist_pop)}")

    print("\n--- Testando __getitem__ (acesso por índice) ---")
    print(f"Primeira música de Rock: {playlist_rock[0]}")
    print(f"Segunda música de Pop: {playlist_pop[1]}")

    print("\n--- Testando __add__ (soma de playlists) ---")
    mix_total = playlist_rock + playlist_pop
    print(f"Nova playlist criada: {mix_total}")
    print(f"Total de músicas no Mix: {len(mix_total)}")
    print(f"Primeira música do Mix: {mix_total[0]}")
    print(f"Última música do Mix: {mix_total[3]}")

