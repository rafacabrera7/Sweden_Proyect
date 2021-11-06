import psycopg2
from datetime import date
from dbSQL import *

def get_customer(id_customer):
# This function takes the id of a customer and return a tuple with its information
# tuple type: (id, Name, email_address, email_password, date(yy,mm,dd))
    try:
        con = psycopg2.connect(user = "postgres",
                               password = "Cabrera05",
                               database = "Sweden",
                               host = "localhost",
                               port = "5432")
        print("Conexión exitosa!")

        con.autocommit = False

        cursor = con.cursor()

        sql_get = """SELECT * FROM customer
                    WHERE id_customer = %s"""

        cursor.execute(sql_get, (id_customer,))
        row = cursor.fetchone()

        con.commit()


    except psycopg2.Error as e:
        print("Error connecting", e)
        con.rollback();

    finally:
        cursor.close()
        con.close()
        print("Conection closed")

    return row
