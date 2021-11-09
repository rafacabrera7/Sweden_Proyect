import psycopg2
from datetime import date
from dbSQL import *

def get_company_report(id_comp):
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
                    SELECT id_job, name_job, description_job, url_job, name_city,date_accesed, name_sector, name_subcategory, email_job, id_company
                    FROM job_offer INNER JOIN company
                    ON id_company_company = id_company
                    INNER JOIN main_sector
                    ON id_sector_main_sector = id_sector
                    INNER JOIN subcategory
                    ON id_subcategory_subcategory = id_subcategory
                    INNER JOIN city
                    ON id_city_city = id_city
                    WHERE id_company = %s
                    ORDER BY date_accesed DESC
                    """
        cursor.execute(sql_get, (id_comp,))


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
