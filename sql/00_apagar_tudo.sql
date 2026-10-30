-- =====================================================================
-- 00_apagar_tudo.sql
-- Apaga as tabelas e as sequences do sistema, para recriar do zero.
-- ORDEM: primeiro a tabela "filha" (PERSONAGENS), que tem as chaves
-- estrangeiras; depois as tabelas "mãe" (JOGADORES e GUILDAS).
-- Se alguma tabela ainda não existir, o Oracle dá erro: pode ignorar.
-- =====================================================================
DROP TABLE PERSONAGENS;
DROP TABLE JOGADORES;
DROP TABLE GUILDAS;
DROP SEQUENCE PERSONAGENS_ID_SEQ;
DROP SEQUENCE JOGADORES_ID_SEQ;
DROP SEQUENCE GUILDAS_ID_SEQ;