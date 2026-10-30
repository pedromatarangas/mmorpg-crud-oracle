from model.personagens import Personagem
from model.jogadores import Jogador
from model.guildas import Guilda
from conexion.oracle_queries import OracleQueries
from utils.entrada import ler_inteiro, ler_texto, perguntar_sim_nao

CLASSES = ["Guerreiro", "Mago", "Arqueiro", "Sacerdote"]


class Controller_Personagem:
    def __init__(self):
        pass

    def buscar_personagem(self, oracle, id_personagem):

        linhas = oracle.consultar(
            f"select p.id_personagem, p.nome, p.classe, p.nivel, "
            f" j.id_jogador, j.nickname, j.email, to_char(j.data_cadastro, 'DD/MM/YYYY'), "
            f" g.id_guilda, g.nome, to_char(g.data_criacao, 'DD/MM/YYYY') "
            f"from personagens p "
            f"inner join jogadores j on j.id_jogador = p.id_jogador "
            f"inner join guildas g on g.id_guilda = p.id_guilda "
            f"where p.id_personagem = {id_personagem}")
        if len(linhas) == 0:
            return None
        linha = linhas[0]
        jogador = Jogador(linha[4], linha[5], linha[6], linha[7])
        guilda = Guilda(linha[8], linha[9], linha[10])
        return Personagem(linha[0], linha[1], linha[2], linha[3], jogador, guilda)
    
    def verifica_existencia_personagem(self, oracle, id_personagem):
        return self.buscar_personagem(oracle, id_personagem) is not None
    
    def listar_personagens(self, oracle):
        return oracle.imprimir(
            "select id_personagem as id, nome, classe, nivel "
            "from personagens order by id_personagem")
    def escolher_classe(self):
        print("Classes disponíveis:")
        for i in range(len(CLASSES)):
            print(f" {i + 1} - {CLASSES[i]}")
        opcao = ler_inteiro(f"Escolha a classe [1-{len(CLASSES)}]: ", 1, len(CLASSES))
        return CLASSES[opcao - 1]
    
    def escolher_jogador(self, oracle):
        print("\nJogadores cadastrados:")
        oracle.imprimir("select id_jogador as id, nickname from jogadores order by id_jogador")
        while True:
            id_jogador = ler_inteiro("ID do jogador dono do personagem: ")
            qtd = oracle.consultar(
                f"select count(1) from jogadores where id_jogador = {id_jogador}")[0][0]
            if qtd > 0:
                return id_jogador
            print(f" Não existe jogador com o ID {id_jogador}.")

    def escolher_guilda(self, oracle):
        print("\nGuildas cadastradas:")
        oracle.imprimir("select id_guilda as id, nome from guildas order by id_guilda")
        while True:
            id_guilda = ler_inteiro("ID da guilda do personagem: ")
            qtd = oracle.consultar(
                f"select count(1) from guildas where id_guilda = {id_guilda}")[0][0]
            if qtd > 0:
                return id_guilda
            print(f" Não existe guilda com o ID {id_guilda}.")

    def existem_jogadores_e_guildas(self, oracle):
        qtd_jogadores = oracle.consultar("select count(1) from jogadores")[0][0]
        qtd_guildas = oracle.consultar("select count(1) from guildas")[0][0]
        if qtd_jogadores == 0 or qtd_guildas == 0:
            print("\nCadastre pelo menos um jogador e uma guilda antes de criar personagens.")
            return False
        return True

    def inserir_personagem(self):
        oracle = OracleQueries()
        while True:
            print("\n=== NOVO PERSONAGEM ===")
            if not self.existem_jogadores_e_guildas(oracle):
                break

            nome = ler_texto("Nome do personagem: ", 30)
            classe = self.escolher_classe()
            nivel = ler_inteiro("Nível [1-100]: ", 1, 100)
            id_jogador = self.escolher_jogador(oracle)
            id_guilda = self.escolher_guilda(oracle)

            novo_id = oracle.proximo_id("PERSONAGENS_ID_SEQ")
            sql = (f"insert into personagens "
                   f"(id_personagem, nome, classe, nivel, id_jogador, id_guilda) "
                   f"values ({novo_id}, '{nome}', '{classe}', {nivel}, {id_jogador}, {id_guilda})")
            if oracle.executar(sql):
                novo_personagem = self.buscar_personagem(oracle, novo_id)
                print("\nPersonagem cadastrado com sucesso!")
                print(novo_personagem.to_string())

            if not perguntar_sim_nao("\nDeseja inserir mais algum personagem?"):
                break
        oracle.fechar()

    def atualizar_personagem(self):
        oracle = OracleQueries()
        while True:
            print("\n=== ATUALIZAR PERSONAGEM ===\n")
            if self.listar_personagens(oracle) == 0:
                print("\nNão há personagens cadastrados.")
                break

            id_personagem = ler_inteiro("\nID do personagem que deseja atualizar: ")
            personagem = self.buscar_personagem(oracle, id_personagem)

            if personagem is None:
                print(f"\nNão existe personagem com o ID {id_personagem}.")
            else:
                print("\nDados atuais: " + personagem.to_string())
                print("Informe os novos dados:")
                novo_nome = ler_texto("Nome do personagem: ", 30)
                nova_classe = self.escolher_classe()
                novo_nivel = ler_inteiro("Nível [1-100]: ", 1, 100)
                novo_jogador = self.escolher_jogador(oracle)
                nova_guilda = self.escolher_guilda(oracle)
                sql = (f"update personagens set nome = '{novo_nome}', "
                       f"classe = '{nova_classe}', nivel = {novo_nivel}, "
                       f"id_jogador = {novo_jogador}, id_guilda = {nova_guilda} "
                       f"where id_personagem = {id_personagem}")
                if oracle.executar(sql):
                    personagem_atualizado = self.buscar_personagem(oracle, id_personagem)
                    print("\nPersonagem atualizado com sucesso!")
                    print(personagem_atualizado.to_string())
            if not perguntar_sim_nao("\nDeseja atualizar mais algum personagem?"):
                break
        oracle.fechar()

    def excluir_personagem(self):
        oracle = OracleQueries()
        while True:
            print("\n=== REMOVER PERSONAGEM ===\n")
            if self.listar_personagens(oracle) == 0:
                print("\nNão há personagens cadastrados.")
                break

            id_personagem = ler_inteiro("\nID do personagem que deseja remover: ")
            personagem = self.buscar_personagem(oracle, id_personagem)

            if personagem is None:
                print(f"\nNão existe personagem com o ID {id_personagem}.")
            else:
                print("\n" + personagem.to_string())
                if not perguntar_sim_nao("Confirma a remoção deste personagem?"):
                    print("\nRemoção cancelada.")
                    break

            if oracle.executar(f"delete from personagens where id_personagem = {id_personagem}"):
                print("\nPersonagem removido com sucesso!")

            if not perguntar_sim_nao("\nDeseja remover mais algum personagem?"):
                break
        oracle.fechar()