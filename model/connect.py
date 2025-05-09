import mariadb

# Connect to MariaDB
def connection():
    try:
        return mariadb.connect(
            user = "root",
            password = "",
            host = "localhost",
            port = 3306,
            database = "login"
        )
    except mariadb.Error as error:
        print(f"Erro ao tentar conectar com o banco. {error}")
        return None