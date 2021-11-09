import psycopg2
from datetime import date
from dbSQL import *
from save_pdf import *

def get_cv_report(id_customer):
# returns a tuple like: (id_job, name_job, description_job, url_job, name_city,date_accesed, name_sector, name_subcategory, email_job, id_company)
    try:
        con = psycopg2.connect(user = "postgres",
                               password = "Cabrera05",
                               database = "Sweden",
                               host = "localhost",
                               port = "5432")
        print("Conexión exitosa!")

        con.autocommit = False

        cursor = con.cursor()

        sql_get = """
                    SELECT id_cv, name_cv FROM resume
                    WHERE id_customer_customer = %s
                    """
        cursor.execute(sql_get, (id_customer,))


        rows = cursor.fetchall()

        return rows

        con.commit()


    except psycopg2.Error as e:
        print("Error connecting", e)
        con.rollback();

    finally:
        cursor.close()
        con.close()
        print("Conection closed")
