from model.jogadores import Jogador
from model.guildas import Guilda

class Personagem:

    def __init__(self, id_personagem=None, nome=None, classe=None, nivel=None, 
                 jogador: Jogador = None, guilda: Guilda = None):
        self.set_id_personagem(id_personagem)
        self.set_nome(nome)
        self.set_classe(classe)
        self.set_nivel(nivel)
        self.set_jogador(jogador)
        self.set_guilda(guilda)

    def set_id_personagem(self, id_personagem):
        self.id_personagem = id_personagem
    def set_nome(self, nome):
        self.nome = nome
    def set_classe(self, classe):
        self.classe = classe
    def set_nivel(self, nivel):
        self.nivel = nivel
    def set_jogador(self, jogador):
        self.jogador = jogador
    def set_guilda(self, guilda):
        self.guilda = guilda
    
    def get_id_personagem(self):
        return self.id_personagem
    def get_nome(self):
        return self.nome
    def get_classe(self):
        return self.classe
    def get_nivel(self):
        return self.nivel
    def get_jogador(self):
        return self.jogador
    def get_guilda(self):
        return self.guilda
    
    def to_string(self):
        return(f"ID: {self.get_id_personagem()} | Nome: {self.get_nome()} | "
               f"Classe: {self.get_classe()} | Nivel: {self.get_nivel()} | "
               f"Jogador: {self.get_jogador().get_nickname()} | "
               f"Guilda: {self.get_guilda().get_nome()}")