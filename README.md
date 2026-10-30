# Sistema de Gerenciamento de MMORPG
Trabalho da disciplina de **Banco de Dados** (FAESA, 2026/2), professor Howard Roatti.

Aplicação de terminal em **Python** que faz o CRUD (inserir, atualizar, remover e relatórios) de um
MMORPG no banco **Oracle**: jogadores, guildas e personagens.

## Integrantes
- Pedro Marques Matarangas
- Davi de Brito Teixeira
- Samuel Floriano Oliveira de Siqueira
- Artur Carmo dos Santos
- Gabriel Leal Hoffoman

## Vídeo de demonstração
[Assista no YouTube](https://www.youtube.com/watch?v=JcYIYt4SRMM)

## Modelo de dados
O sistema tem três tabelas. Um jogador possui vários personagens e uma guilda agrupa vários personagens;
cada personagem pertence a um jogador e a uma guilda.
| Tabela | Colunas |
|---|---|
| GUILDAS | ID_GUILDA (PK), NOME (único), DATA_CRIACAO |
| JOGADORES | ID_JOGADOR (PK), NICKNAME (único), EMAIL, DATA_CADASTRO |
| PERSONAGENS | ID_PERSONAGEM (PK), NOME, CLASSE, NIVEL, ID_JOGADOR (FK), ID_GUILDA (FK) |
O diagrama relacional está em [diagrams/diagrama_relacional.png](diagrams/diagrama_relacional.png).

## Organização

- `diagrams/`: diagrama relacional (imagem e código Mermaid).
- `sql/`: scripts de criação das tabelas, sequences, relacionamentos e dados de exemplo, numerados na
ordem de execução.
- `src/conexion/`: classe de conexão com o Oracle.
- `src/model/`: classes das entidades (Guilda, Jogador, Personagem).
- `src/controller/`: classes que inserem, atualizam e removem registros.
- `src/reports/` e `src/sql/`: relatórios e suas consultas SQL.
- `src/utils/`: menus, splash screen e leitura de dados do teclado.
- `src/principal.py`: programa principal.

## Como executar (Linux, na VM da disciplina)

### 1. Baixar o projeto

```bash
git clone https://github.com/pedromatarangas/mmorpg-crud-oracle.git
cd mmorpg-crud-oracle/src
```

### 2. Instalar a biblioteca de conexão

O projeto usa a biblioteca `oracledb` para conectar ao Oracle. Para instalar a `oracledb`:

```bash
pip3 install -r requirements.txt --break-system-packages
```

### 3. Conferir os dados de conexão

Os dados ficam no topo do arquivo `src/conexion/oracle_queries.py` (usuário, senha, host, porta e service name).
Por padrão: usuário `labdatabase`, `localhost`, porta `1521`,  service name `XEPDB1`. Para testar a conexão:

```bash
python3 teste_conexao.py
```

### 4. Criar as tabelas e os dados de exemplo

```bash
python3 criar_tabelas.py
```

Alternativa: executar no DBeaver ou SQL Developer os scripts da pasta `sql/`, nesta ordem:
`00_apagar_tudo.sql`, `01_guildas.sql`, `02_jogadores.sql`, `03_personagens.sql`.

### 5. Executar o sistema

```bash
python3 principal.py
```

## Como usar

Ao iniciar, a tela inicial mostra o total de registros de cada tabela. No menu principal:

1. **Relatórios:** personagens por classe (agrupamento), personagens por guilda (agrupamento com junção)
e lista completa de personagens (junção).
2. **Inserir registros:** escolha a tabela e informe os dados pedidos.
3. **Atualizar registros:** escolha a tabela, o registro pelo ID e informe os novos dados.
4. **Remover registros:** escolha a tabela e o registro pelo ID. Ao remover um jogador ou uma guilda que
tem personagens, o sistema pergunta se deve removê-los junto.
5. **Sair.**

## Uso de IA

Os prompts usados como apoio estão registrados em [PROMPTS.md](PROMPTS.md).