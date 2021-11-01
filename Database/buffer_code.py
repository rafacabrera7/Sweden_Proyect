import psycopg2
from datetime import date
from dbSQL import *

#tuple will be like: (i["id"] , i["title"], i["description"], i["email"] , i["entity"], date_accesed , i["url"], customer, main_sector, subcategory)

def insert_application(tuple):
    #tuple recieved is of the form: (id_customer, id_job_offer)
    # this function recieves one tuple and inserts the value corresponding to
    # name_customer in the table customer
    # since id_customer should be automatically generated, it returns that
    # id to be used later.
    # in case the customer has already been insert, it searches for its id
    # and returns it.
    #it returns a tuple with id_customer and id_job

    try:
        con = psycopg2.connect(user = "postgres",
                               password = "Cabrera05",
                               database = "Sweden",
                               host = "localhost",
                               port = "5432")
        print("Conexión exitosa!")

        con.autocommit = False

        cursor = con.cursor()

        f_tuple = tuple + (date.today(),)

        sql_insert = """INSERT INTO application VALUES (%s, %s, %s)
                        RETURNING *"""

        cursor.execute(sql_insert,f_tuple)
        id_application = cursor.fetchone()
        id_application = (id_application[0],id_application[1])

        con.commit()
        print("application inserted")
        return id_application

    except psycopg2.Error as e:
        print("Error connecting", e)
        con.rollback();

    finally:
        cursor.close()
        con.close()
        print("Conection closed")

t = (1,123)
print(insert_application(t))
