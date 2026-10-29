--	=====================================================================
--  01_guildas.sql	
--  Cria	a	tabela	GUILDAS,	a	sequence	que	gera	os	IDs	e	insere	dados	de	exemplo.  
--  Deve	ser	executado	ANTES	do	03_personagens.sql.
--	=====================================================================
--  Tabela	GUILDAS:	os	clãs	do	jogo
CREATE	TABLE	GUILDAS	(
	ID_GUILDA        NUMBER(10)    NOT	NULL,
	NOME	         VARCHAR2(50)  NOT	NULL,
	DATA_CRIACAO     DATE		   NOT	NULL,
	CONSTRAINT GUILDAS_PK	       PRIMARY	KEY	(ID_GUILDA),
	CONSTRAINT GUILDAS_NOME_UK	   UNIQUE  (NOME)
);

--	Sequence:	um	contador	que	entrega	1,	2,	3...	para	usar	como	ID
CREATE	SEQUENCE	GUILDAS_ID_SEQ;

--	Dados	de	exemplo
INSERT	INTO	GUILDAS	(ID_GUILDA,	NOME,	DATA_CRIACAO)
VALUES	(GUILDAS_ID_SEQ.NEXTVAL,	'Touros Negros',	TO_DATE('15/01/2026',	'DD/MM/YYYY'));
INSERT	INTO	GUILDAS	(ID_GUILDA,	NOME,	DATA_CRIACAO)
VALUES	(GUILDAS_ID_SEQ.NEXTVAL,	'Alvorecer Dourado',	TO_DATE('03/02/2026',	'DD/MM/YYYY'));
INSERT	INTO	GUILDAS	(ID_GUILDA,	NOME,	DATA_CRIACAO)
VALUES	(GUILDAS_ID_SEQ.NEXTVAL,	'Aguias de Prata',	TO_DATE('20/03/2026',	'DD/MM/YYYY'));
INSERT	INTO	GUILDAS	(ID_GUILDA,	NOME,	DATA_CRIACAO)
VALUES	(GUILDAS_ID_SEQ.NEXTVAL,	'Leoes Carmesins',	TO_DATE('11/05/2026',	'DD/MM/YYYY'));
COMMIT;