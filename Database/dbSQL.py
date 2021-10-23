import psycopg2
from connection import Connection

def insert_companies(tuples):
    try:
        con = psycopg2.connect(user = "postgres",
                               password = "Cabrera05",
                               database = "Sweden",
                               host = "localhost",
                               port = "5432")
        print("Conexión exitosa!")

        con.autocommit = False

        cursor = con.cursor()

        sql = """INSERT INTO company VALUES (DEFAULT, %s)"""

        companies = ()
        for tuple in tuples:
            cursor.execute(sql, (tuple[0],))

        con.commit()

        print("Insertion completed!")

    except psycopg2.Error as e:
        print("Error connecting", e)
        conexion.rollback();

    finally:
        cursor.close()
        con.close()
        print("Conection closed")

companies = [('Test1',),('K\u00f6ksbitr\u00e4de till',),('Test3',),('Test4',),('Test1',)]
insert_companies(companies)
