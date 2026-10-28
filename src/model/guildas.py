# =====================================================================
# guildas.py
# Classe que representa UMA linha da tabela GUILDAS.
# =====================================================================
class Guilda:
    def __init__(self, id_guilda=None, nome=None, data_criacao=None):
        self.set_id_guilda(id_guilda)
        self.set_nome(nome)
        self.set_data_criacao(data_criacao)

    # ---------- setters ----------
    def set_id_guilda(self, id_guilda):
        self.id_guilda = id_guilda

    def set_nome(self, nome):
        self.nome = nome

    def set_data_criacao(self, data_criacao):
        self.data_criacao = data_criacao

    # ---------- getters ----------
    def get_id_guilda(self):
        return self.id_guilda

    def get_nome(self):
        return self.nome

    def get_data_criacao(self):
        return self.data_criacao

    # ---------- to_string ----------
    def to_string(self):
        return f"ID: {self.get_id_guilda()} | Nome: {self.get_nome()} | Criada em: {self.get_data_criacao()}"