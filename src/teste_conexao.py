# Testa se o Python consegue conversar com o Oracle.
# Rode de dentro da pasta src: python3 teste_conexao.py

from conexion.oracle_queries import OracleQueries

oracle = OracleQueries()
resultado = oracle.consultar("select 'Conexao funcionando!' from dual")
print(resultado[0][0])
