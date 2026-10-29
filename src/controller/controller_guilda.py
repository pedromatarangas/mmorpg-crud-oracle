# =====================================================================
# controller_guilda.py
# Inserir, atualizar e remover GUILDAS, conversando com o usuário
# e montando os comandos SQL como texto.
# =====================================================================
from model.guildas import Guilda
from conexion.oracle_queries import OracleQueries
from utils.entrada import ler_inteiro, ler_texto, ler_data, perguntar_sim_nao


class Controller_Guilda:

    def __init__(self):
        pass

    # ----------------------------------------------------------------
    # Funções de apoio (usadas pelas funções principais lá embaixo)
    # ----------------------------------------------------------------
    def buscar_guilda(self, oracle, id_guilda):
        """Busca a guilda pelo ID. Devolve um objeto Guilda, ou None se não existir."""
        linhas = oracle.consultar(
            f"select id_guilda, nome, to_char(data_criacao, 'DD/MM/YYYY') "
            f"from guildas where id_guilda = {id_guilda}"
        )
        if len(linhas) == 0:
            return None
        linha = linhas[0]
        return Guilda(linha[0], linha[1], linha[2])

    def verifica_existencia_guilda(self, oracle, id_guilda):
        """Devolve True se existe guilda com esse ID."""
        return self.buscar_guilda(oracle, id_guilda) is not None

    def nome_ja_usado(self, oracle, nome, ignorar_id=None):
        """Devolve True se outra guilda já usa esse nome."""
        sql = (
            f"select count(1) from guildas where upper(nome) = upper('{nome}')"
        )
        if ignorar_id is not None:
            sql = sql + f" and id_guilda <> {ignorar_id}"
        return oracle.consultar(sql)[0][0] > 0

    def listar_guildas(self, oracle):
        """Mostra as guildas na tela e deolve quantas existem."""
        return oracle.imprimir(
            "select id_guilda as id, nome from guildas order by id_guilda"
        )

    # ----------------------------------------------------------------
    # INSERIR
    # ----------------------------------------------------------------
    def inserir_guilda(self):
        oracle = OracleQueries()
        while True:
            print("\n=== NOVA GUILDA ===")
            nome = ler_texto("Nome da guilda: ", 50)
            if self.nome_ja_usado(oracle, nome):
                print(f"\nJá existe uma guilda chamada '{nome}'.")
            else:
                data_criacao = ler_data("Data de criação")
                novo_id = oracle.proximo_id("GUILDAS_ID_SEQ")
                sql = (
                    f"insert into guildas (id_guilda, nome, data_criacao) "
                    f"values ({novo_id}, '{nome}', to_date('{data_criacao}', 'DD/MM/YYYY'))"
                )
                if oracle.executar(sql):
                    nova_guilda = self.buscar_guilda(oracle, novo_id)
                    print("\nGuilda cadastrada com sucesso!")
                    print(nova_guilda.to_string())
            if not perguntar_sim_nao("\nDeseja inserir mais alguma guilda?"):
                break
        oracle.fechar()

    # ----------------------------------------------------------------
    # ATUALIZAR
    # ----------------------------------------------------------------
    def atualizar_guilda(self):
        oracle = OracleQueries()
        while True:
            print("\n=== ATUALIZAR GUILDA ===\n")
            if self.listar_guildas(oracle) == 0:
                print("\nNão há guildas cadastradas.")
                break
            id_guilda = ler_inteiro("\nID da guilda que deseja atualizar: ")
            guilda = self.buscar_guilda(oracle, id_guilda)
            if guilda is None:
                print(f"\nNão existe guilda com o ID {id_guilda}.")
            else:
                print("\nDados atuais: " + guilda.to_string())
                print("Informe os novos dados:")
                novo_nome = ler_texto("Nome da guilda: ", 50)
                if self.nome_ja_usado(oracle, novo_nome, id_guilda):
                    print(f"\nJá existe outra guilda chamada '{novo_nome}'.")
                else:
                    nova_data = ler_data("Data de criação")
                    sql = (
                        f"update guildas set nome = '{novo_nome}', "
                        f"data_criacao = to_date('{nova_data}', 'DD/MM/YYYY') "
                        f"where id_guilda = {id_guilda}"
                    )
                    if oracle.executar(sql):
                        guilda_atualizada = self.buscar_guilda(
                            oracle, id_guilda
                        )
                        print("\nGuilda atualizada com sucesso!")
                        print(guilda_atualizada.to_string())
            if not perguntar_sim_nao("\nDeseja atualizar mais alguma guilda?"):
                break
        oracle.fechar()

    # ----------------------------------------------------------------
    # REMOVER
    # ----------------------------------------------------------------
    def excluir_guilda(self):
        oracle = OracleQueries()
        while True:
            print("\n=== REMOVER GUILDA ===\n")
            if self.listar_guildas(oracle) == 0:
                print("\nNão há guildas cadastradas.")
                break
            id_guilda = ler_inteiro("\nID da guilda que deseja remover: ")
            guilda = self.buscar_guilda(oracle, id_guilda)
            if guilda is None:
                print(f"\nNão existe guilda com o ID {id_guilda}.")
            else:
                print("\n" + guilda.to_string())
                if not perguntar_sim_nao("Confirma a remoção desta guilda?"):
                    print("\nRemoção cancelada.")
                    break  # o edital pede: se "Não", volta ao menu principal
              
                # A guilda é chave estrangeira em PERSONAGENS?
                qtd = oracle.consultar(f"select count(1) from personagens where id_guilda = {id_guilda}")[0][0]
                
                if qtd > 0:
                    # Tem personagens: a guilda NÃO pode ser excluída
                    print(f"\nA guilda '{guilda.get_nome()}' não pode ser excluída, "
                          f"porque ainda tem {qtd} personagem(ns):\n")
                    oracle.imprimir(
                        f"select id_personagem as id, nome from personagens "
                        f"where id_guilda = {id_guilda} order by id_personagem")
                    print("\nTransfira esses personagens para outra guilda "
                          "(menu Atualizar > Personagens) e tente novamente.")
                else:
                    if oracle.executar(f"delete from guildas where id_guilda = {id_guilda}"):
                        print("\nGuilda removida com sucesso!")
            if not perguntar_sim_nao("\nDeseja remover mais alguma guilda?"):
                break
        oracle.fechar()
                        