import csv
import mysql.connector

# estabeleça a conexão com o banco de dados
conn = mysql.connector.connect(user='raffDV', password='QQ9HY4z5!B*5!f^j',
                               host='localhost', database='GeoLoc')

# abra o arquivo CSV
with open('./input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # pule a primeira linha (cabeçalho)
            line_count += 1
        else:
            # execute o INSERT para a linha atual
            cursor = conn.cursor()
            sql = "INSERT INTO aux_geolite2CityLocationsEn (geoname_id, locale_code, continent_code, continent_name, country_iso_code, country_name, subdivision_1_iso_code, subdivision_1_name, subdivision_2_iso_code, subdivision_2_name, city_name, metro_code, time_zone, is_in_european_union) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
            cursor.execute(sql, values)
            conn.commit()
            print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}")
            line_count += 1


# feche a conexão com o banco de dados
conn.close()
