import csv
import mysql.connector
import time

# Estabeleça a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="raffDV",
    password="QQ9HY4z5!B*5!f^j",
    database="GeoLoc"
)

# Crie um cursor para executar comandos SQL
cursor = conexao.cursor()

# Defina a consulta SQL com a sintaxe do multi-value insert
sql = "INSERT INTO aux_IPv4Blocks (network, geoname_id, registered_country_geoname_id, represented_country_geoname_id, is_anonymous_proxy, is_satellite_provider, postal_code, latitude, longitude, accuracy_radius) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Abra o arquivo CSV com os dados a serem inseridos
with open('input.csv') as arquivo:
    leitor_csv = csv.reader(arquivo)
    inicio = time.time()
    
    # Inicie a inserção das linhas do arquivo CSV em grupos de 50.000
    contador_linhas = 0
    valores = []
    for linha in leitor_csv:
        valores.append(tuple(linha))
        contador_linhas += 1
        
        # Quando a lista de valores atingir 50.000, execute a consulta SQL e reinicie a lista de valores
        if contador_linhas == 50000:
            cursor.executemany(sql, valores)
            conexao.commit()
            valores = []
            contador_linhas = 0
           
    
    # Se ainda houver valores restantes na lista de valores, execute a consulta SQL
    if valores:
        cursor.executemany(sql, valores)
        conexao.commit()
    tempo_total = time.time() - inicio
    print(f"A inserção de {len(valores)} linhas demorou {tempo_total:.2f} segundos.")


# Feche o cursor e a conexão
cursor.close()
conexao.close()
