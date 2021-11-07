import psycopg2
from datetime import date
from dbSQL import *

def get_jobs(id_sector, id_subcategory, n_jobs):
# This function takes the id of a jobs and return a text with its information

    try:
        con = psycopg2.connect(user = "postgres",
                               password = "Cabrera05",
                               database = "Sweden",
                               host = "localhost",
                               port = "5432")
        print("Conexión exitosa!")

        con.autocommit = False

        cursor = con.cursor()

        sql_get = """SELECT *
FROM job_offer LEFT JOIN application
ON id_job = id_job_job_offer
"""
        # MISSING INNER JOIN TO NOT REPEAT APPLYING TO A JOB OFFER.

        cursor.execute(sql_get, (id_sector,id_subcategory, n_jobs))
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
get_jobs(4,3,3)
