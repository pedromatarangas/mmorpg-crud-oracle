# Registro de uso de IA

Conforme o edital, registramos aqui os prompts utilizados como apoio ao desenvolvimento,
a ferramenta usada e o que o grupo fez com cada resposta.

## Pedro Marques Matarangas

### Prompt 1 — 27/10/2026
**Fonte:** Claude Opus 5.5 (Anthropic)

**Prompt:**
```text
Claude, estou fazendo um trabalho em grupo de banco de dados para a faculdade, onde teremos que mesclar um CRUD em Python com criação de tabelas, relacionamentos de banco de dados e afins. Porém o professor pede pra usarmos um repositório Git pro grupo, com os integrantes e o professor de colaboradores. Utilizamos uma máquina virtual linux que o próprio professor disponibiliza, nela já tem Git, VSCode, Python, acesso ao banco de dados Oracle e afins. Preferivelmente faríamos em Java, mas acho que daria trabalho em relação a VM, e o próprio exemplo dado pelo professor foi em Python. A parte que pega mais é a questão do Git, preciso que me explique passo a passo, para que eu crie o repositório, consiga clonar ele na máquina, assim como pros demais integrantes que cada um vai fazer ná sua, me explique como fazer os commits, pull, tudo que preciso saber pra dar certo. No edital fala também que precisaremos de um arquivo PROMPTS.md no repositório, com o registro de uso de IA, especificamente dos prompts usados. Segue o link de exemplo do professor.
https://github.com/howardroatti/example_crud_oracle
```

**O que foi feito com a resposta:** Criação do repositório no GitHub, criação da estrutura inicial de arquivos, aprendizado dos comandos básicos do Git.

---

### Prompt 2 - 27/10/2026
**Fonte:** Claude Opus 5.5 (Anthropic)

**Prompt:**
```text
Ta, estamos alinhados agora. Como será feita a divisão, qual seria mais ou menos a ideia. Me explica como está o projeto exemplo do professor, só pra eu entender mais ou menos. Não quero que me de código de nada, só quero que me explique o passo a passo, o que seria recomendado fazer primeiro. Estou pensando em ficar encarregado da parte de Python, e passar o SQL pros outros integrantes fazerem. O tema seria MMORPG, normalmente eu sou criativo o suficiente pra pensar em alguma coisa, mas como eu sinceramente não entendi muito bem a proposta ainda do trabalho, gostaria que me explicasse, como funcionaria as questões da tabela, qual o objetivo etc.
```

**O que foi feito com a resposta:** Aprendizado do esquema do trabalho, definição dos papéis dos integrantes do grupo. Claude recomendou não fazer a parte de Python sozinho, pois ficaria desigual. Explicou sobre as tabelas que seriam criadas e seus relacionamentos.

---

### Prompt 3 - 27/10/2026
**Fonte:** Claude Opus 5.5 (Anthropic)

**Prompt:**
```text
Beleza claude, eu entendi mais ou menos 15% de tudo que você falou. Vamos por parte, primeiro você tem que lembrar que, nas nossas aulas a gente simplesmente seguia um roteiro, ficava copiando CREATE TABLE, INSERT, SELECT, de um exemplo já existente, só alterando os atributos de cada um, que também eram nos fornecido. Literalmente um trabalho extremamente automatico, que particularmente, mesmo fazendo tudo, conituava sem enteder direito. Depois que montamos os scripts a gente fez uns "exercícios" que eram pra rodar comandos, que por exemplo mostrassem "pessoas que tem Maria no nome", ou algo por ai. Que temos até de outras conversas ai que te mandava pra tirar duvida. Então assim, literalmente você tem que explicar TUDO, DESTRINCHADO, como se estivesse explicando pra alguem de 5 anos de idade. Detalhe, quando entramos na parte de Python, aí a coisa fica feia. Tudo que sabemos é Java, temos a lógica, mas 0 domínio da linguagem em si, ainda mais se tratando de coisas de que nem em Java vimos como fazer ainda. Por isso tinha me proposto a cuidar dessa parte em especifico. Qual a relação com banco de dados, eu vou criar uma classe Guilda, o que precisa? Tem construtor ou nao tem contrutor, os atributos sao os mesmos que tem que estar na tabela, tem algum método, como define a interação do python com as tabelas em sql/oracle? Agora outra coisa por exemplo, clonamos o repositorio, todo mundo de acordo e tals, mas isso ele ta no VSCode, como que faz pra criar um arquivo .sql no DBEAVER e dar push sendo que a pasta ta no VSCode só. Vamos fazer o SQL pelo proprio VScode depois so testar no DBEAVER? Tem que ter esses nuances, que nem com as ferramentas sabemos mexer direito, e isso do git deixa tudo pior. É MUITA coisa que ninguem sabe. Então por favor, se puder inclusive, destrinchar a parte de cada um em um PDF separado pra cada, explicando passo a passo, seria de grande ajuda.
```

**O que foi feito com a resposta:** Criação de 5 arquivos PDF, designados um para cada membro do grupo, definindo o que teriam que fazer. A parte inicial é comum pra todos, que conta com explicações sobre banco de dados, python, git e afins.

---

### Prompt 4 - 30/10/2026
**Fonte:** Claude Opus 5.5 (Anthropic)

**Prompt:**
```text
Bom dia Claudinho, preciso fazer a Splash Screen do trabalho, mas queria deixar ela mais enfeitada pro tema em questão. Em se tratando de MMORPG, pensei naquelas Splash Screens antigas estilo fliperama, acho que cairia bem legal no projeto. Eu literalmente não sei como faz uma, então se pudesse fazer pra mim, aproveito e dou uma estudada em cima.
```

**O que foi feito com a resposta:** Código da Splash Screen.

---

## Davi de Brito Teixeira 

### Prompt 1 - 28/10/2026
**Fonte:** Gemini

**Prompt:**
```text
Gemini, estou fazendo um trabalho de banco de dados na VM oracle e estou na parte de fazer o teste SQL pra ver se ta rodando essa parte. Fiz o passo a passo aqui para conseguir abrir o arquivo no DBeaver e apertei o Alt+X pra ver a conexao, porem deu "No active connection". Depois disso consegui conectar e fazer os testes.
```

**O que foi feito com a resposta:** Testes no DBeaver sobre o SQL de GUILDAS.

---

### Prompt 2 - 28/10/2026
**Fonte:** Gemini

**Prompt:**
```text
Gemini, gostaria de saber se tem alguma forma de fazer a identação do código dentro do VS Code na VM ou teria que fazer tudo manualmente.
```

**O que foi feito com a resposta:** Foi feito a identação do código na parte de model Guildas.

---

### Prompt 3 - 28/10/2026
**Fonte:** Gemini

**Prompt:**
```text
Gemini, estou na parte da criação de Controller da Guilda. Vou mandar o codigo para que possa me ajudar caso encontre algum erro e tambem vou precisar de ajuda na parte da identação do codigo para usar no VS Code da VM.
```

**O que foi feito com a resposta:** Foi feita uma verificação do codigo na parte de Controller Guilda e feita a identação correta para usar no VS Code da VM.

---

## Samuel Floriano Oliveira de Siqueira

### Prompt 1 - 28/10/2026
**Fonte:** Claude Sonnet 5.5 Medium

**Prompt:**
```text
Estou fazendo um trabalho em grupo de Banco de Dados (projeto mmorpg-crud-oracle, em Python) e criei a classe Jogador em src/model/jogadores.py, com getters, setters e to_string. Rodei git pull, git add src/model/jogadores.py e git commit, mas a máquina virtual travou no meio do git add. Agora, ao rodar git push, aparece: fatal: unable to read 49cc4ca..., the remote end hung up unexpectedly e failed to push some refs. Já tentei git reset --soft HEAD~1 e git pull, e nada mudou. Como resolvo esse erro e consigo enviar meu código para o repositório?
```

**O que foi feito com a resposta:** Segui as orientações da IA no terminal. Primeiro rodei git fsck, que confirmou o missing blob. Depois executei git reset --soft HEAD~1, git reset e git add src/model/jogadores.py, o que regravou o objeto que faltava. Rodei o git fsck de novo e ele não apontou mais erros. Por fim, fiz o git commit e o git push, e o código foi enviado ao repositório com sucesso.

---

## Artur Carmo dos Santos

### Prompt 1 - 29/10/2026
**Fonte:** Claude Opus 5.5 (Anthropic)

**Prompt:**
```text
oq tem de errado no meu código? o id_personagem no começo ta com uma linha ondulada embaixo
[código da classe Personagem colado junto]
```

**O que foi feito com a resposta:** Entendi e corrigi três erros na classe Personagem. (1) O parâmetro do construtor foi digitado como "id_personagempo", então a variável id_personagem usada na linha de baixo não existia (era a linha ondulada). (2) No construtor eu chamava self.get_guilda(guilda), mas o construtor precisa guardar o valor, então o certo é o setter, self.set_guilda(guilda). (3) O get_id_personagem recebia um parâmetro a mais; getters só recebem o self, e o to_string() chamava ele sem argumento, o que daria erro. Depois de corrigir, testei o import da classe e fiz o commit do model.

---

### Prompt 2 - 29/10/2026
**Fonte:** Claude Opus 5.5 (Anthropic)

**Prompt:**
```text
como faz para teste o controller?
```

**O que foi feito com a resposta:** Segui o roteiro de testes do Controller_Personagem. Os erros que apareceram foram de ambiente, não do código: faltava a biblioteca oracledb (instalei com pip3), o Oracle estava desligado no Docker (subi com docker compose up -d) e as tabelas não existiam no meu banco (ORA-00942), porque o Git compartilha os arquivos .sql, mas cada VM tem o próprio banco e precisa executar os scripts.

### Observação
Minha parte (Integrante C: script SQL da tabela PERSONAGENS, classe Personagem e Controller_Personagem) foi feita seguindo o guia em PDF gerado pelo Claude a partir do Prompt 3 do Pedro.

---

## Gabriel Leal Hoffoman

### Prompt 1 - 28/10/2026
**Fonte:** Gemini

**Prompt:**
```text
Gemini, poderia corrigir todo o projeto que irei lhe enviar a seguir, sendo tema MMORPG, veja se tem algo incorreto e me explique o que deveria ter sido feito para executar com excelência. Incluindo os códigos.
```
**O que foi feito com a resposta:** As informações fornecidas pela IA foi utilizada por várias consultas que não tinham ";" no final, que ocorre erro de sintexe, me compilou os arquivos necessários já que não estava conseguindo e também corrigiu o código do diagrama mermaid.

---

### Prompt 2 - 28/10/2026
**Fonte:** Gemini

**Prompt:**
```text
Gemini, surgiu uma certa dúvida de como eu poderia fazer um bom roteiro de vídeo que envolva testar o sistema produzido pelo grupo, incluindo menus de inserção, atualização, remoção, relatórios e tela inicial, como dito anteriormente por você. Seria agradável também sugerir um exemplo de roteiro para compreensão melhor desta etapa do trabalho.
```

**O que foi feito com a resposta:** O modelo de roteiro fornecido pela IA foi utilizado como base para criar e estruturar o arquivo `ROTEIRO_VIDEO.md` na raiz do projeto, dividindo os tempos e falas da apresentação entre os integrantes do grupo para a gravação da demonstração do sistema.

