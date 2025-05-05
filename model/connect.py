import mariadb

# Connect to MariaDB
def connection():
    try:
        return mariadb.connect(
            user = "root",
            password = "dimebag1966",
            host = "localhost",
            port = 8080,
            database = "login"
        )
    except mariadb.Error as error:
        print(f"Erro ao tentar conectar com o banco. {error}")
        return None