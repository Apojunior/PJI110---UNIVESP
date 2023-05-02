import psycopg2

# Conecta no banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="senha123"
)

# Cria um cursor
cur = conn.cursor()

# Executa uma consulta
cur.execute("SELECT * FROM projetointegrador_cliente")

# Recupera os resultados
rows = cur.fetchall()

# Imprime os resultados
for row in rows:
    print(row)

# Fecha o cursor e a conexão
cur.close()
conn.close()
