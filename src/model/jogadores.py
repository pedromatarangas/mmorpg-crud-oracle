class Jogador:
    def __init__(self, id_jogador=None, nickname=None, email=None, data_cadastro=None):
        self.set_id_jogador(id_jogador)
        self.set_nickname(nickname)
        self.set_email(email)
        self.set_data_cadastro(data_cadastro)

        #-----setters-----
    def set_id_jogador(self, id_jogador):
        self.id_jogador = id_jogador

    def set_nickname(self, nickname):
        self.nickname = nickname
    
    def set_email(self, email):
        self.email = email

    def set_data_cadastro(self, data_cadastro):
        self.data_cadastro = data_cadastro

    #-----getters-----
    def get_id_jogador(self):
        return self.id_jogador
    
    def get_nickname(self):
        return self.nickname
    
    def get_email(self):
        return self.email
    
    def get_data_cadastro(self):
        return self.data_cadastro
    #-----to string-----
    def to_string(self):
        return(f"ID: {self.get_id_jogador()} | Nickname: {self.get_nickname()} | "
    f"E-mail: {self.get_email()} | Cadastro {self.get_data_cadastro()}")