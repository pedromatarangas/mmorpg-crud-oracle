from model.jogadores import Jogador
from conexion.oracle_queries import OracleQueries
from utils.entrada import ler_inteiro, ler_texto, ler_data, perguntar_sim_nao

class Controller_Jogador:
        def __init__(self):
                pass

        
        def buscar_jogador(self, oracle, id_jogador):
                """Busca o jogador pelo ID. Devolve um objeto Jogador, ou None se nao existir"""
                
                linhas = oracle.consultar(
                        f"select id_jogador, nickname, email, to_char(data_cadastro, 'DD/MM/YYYY') "
                        f"from jogadores where id_jogador = {id_jogador}")
                if len(linhas) == 0:
                        return None
                linha = linhas[0]
                return Jogador(linha[0], linha[1], linha[2], linha[3])

        def verifica_existencia_jogador(self, oracle, id_jogador):
                """Devolve True se existe jogador com esse ID"""
                return self.buscar_jogador(oracle, id_jogador) is not None

        def nickname_ja_usado(self, oracle, nickname, ignorar_id=None):
                """Devolve True se outro jogador já tiver esse nome"""
                sql = f"select count(1) from jogadores where upper(nickname) = upper('{nickname}')"
                if ignorar_id is not None:
                        sql = sql + f" and id_jogador <> {ignorar_id}"
                return oracle.consultar(sql)[0][0] > 0

        def ler_email(self):
                """lê um e-mail e confere se tem '@'."""
                while True:
                        email = ler_texto("E-mail: ", 100)
                        if "@" in email:
                                return email
                        print(" E-mail inválido: precisa ter o '@'.")

        def listar_jogadores(self, oracle):
                return oracle.imprimir("select id_jogador as id, nickname from jogadores order by id_jogador")

        #INSERIR

        def inserir_jogador(self):
                oracle = OracleQueries()
                while True:
                        print("\n=== NOVO JOGADOR ===")
                        nickname = ler_texto("Nickname: ", 30)

                        if self.nickname_ja_usado(oracle, nickname):
                                print(f"\nO nickname '{nickname}' já está em uso. ")
                        else:
                                email = self.ler_email()
                                data_cadastro = self.ler_email()
                                novo_id = oracle.proximo_id("JOGADORES_ID_SEQ")
                                sql = (f"insert into jogadores (id_jogador, nickname, email, data_cadastro) "
                                       f"values ({novo_id}, '{nickname}', '{email}', "
                                       f"to_date('{data_cadastro}', 'DD/MM/YYYY'))")

                                if oracle.executar(sql):
                                        novo_jogador = self.buscar_jogador(oracle, novo_id)
                                        print("\nJogador cadastrado com sucesso! ")
                                        print(novo_jogador.to_string())
                        
                        if not perguntar_sim_nao("\nDeseja inserir mais algum jogdor?"):
                                break
                oracle.fechar()

        #ATUALIZAR

        def atualizar_jogador(self):
                oracle = OracleQueries()
                while True:
                        print("\n=== ATUALIZAR JOGADOR ===\n")
                        if self.listar_jogadores(oracle) == 0:
                                print("\nNão há jogadores cadastrados. ")
                                break

                        id_jogador = ler_inteiro("\nID do jogador que deseja atualizar: ")
                        jogador = self.buscar_jogador(oracle, id_jogador)

                        if jogador is None:
                                print(f"\nNão existe jogador com esse ID {id_jogador}.")
                        else:
                                print("\nDados atuais: " + jogador.to_string())
                                print("Informe os novos dados: ")
                                novo_nickname = ler_texto("Nickname: ", 30)
                                if self.nickname_ja_usado(oracle, novo_nickname, id_jogador):
                                        print(f"\nO nickname '{novo_nickname}' já está em uso por outro jogador. ")
                                else:
                                        novo_email = self.ler_email()
                                        nova_data = ler_data()
                                        sql = (f"update jogadores set nickname = '{novo_nickname}', "
                                               f"email = '{novo_email}', "
                                               f"data_cadastro = to_date('{nova_data}', 'DD/MM/YYYY') "
                                               f"where id_jogador = {id_jogador}")
                                        if oracle.executar(sql):
                                                jogador_atualizado = self.buscar_jogador(oracle, id_jogador)
                                                print("\nJogador atualizado com sucesso! ")
                                                print(jogador_atualizado.to_string())

                        if not perguntar_sim_nao("\nDeseja atualziar mais algum jogador?"):
                                break
                oracle.fechar()

        #REMOVER

        def excluir_jogador(self):
                oracle = OracleQueries()
                while True:
                        print("\n=== REMOVER JOGADOR ===")
                        if self.listar_jogadores(oracle) == 0:
                                print("\nNão há jogadores cadastrados. ")
                                break
                        id_jogador = ler_inteiro("\nID do jogador que deseja remover: ")
                        jogador = self.buscar_jogador(oracle, id_jogador)

                        if jogador is None:
                                print(f"\nNão existe jogador com o ID {id_jogador}.")
                        else:
                                print("\n" + jogador.to_string())
                                if not perguntar_sim_nao("Confirmar a remoção deste jogador?"):
                                        print("\nRemoção cancelada.")
                                        break

                                qtd = oracle.consultar(
                                        f"select count(1) from personagens where id_jogador = {id_jogador}")[0][0]

                                if qtd > 0:
                                        print("\nO jogador não foi removido, porque ainda tem personagens. ")
                                        if perguntar_sim_nao("Deseja remover esses personagens junto com o jogador?"):
                                                oracle.executar(f"delete from personagens where id_jogador = {id_jogador}")
                                                if oracle.executar(f"delete from jogadores where id_jogador = {id_jogador}"):
                                                        print(f"\nJogador e {qtd} personagem(ns) removidos com sucesso! ")
                                                else:
                                                        print("\nO jogador não foi removido, porque ainda tem personagens.")
                                else:
                                    if oracle.executar(f"delete from jogadores where id_jogador = {id_jogador}"):
                                        print("\nJogador removido com sucesso!")

                        if not perguntar_sim_nao("Deseja remover mais algum jogador?"):
                                break
                oracle.fechar()
                