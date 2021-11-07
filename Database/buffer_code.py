import psycopg2
from datetime import date
from dbSQL import *

def get_jobs(id_customer, id_sector, id_subcategory, n_jobs):
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

        if id_subcategory != None:
            sql_get = """
                        SELECT *
                        FROM (
                        SELECT DISTINCT ON (id_job) id_job, name_job, description_job, email_job, id_company_company, id_sector_main_sector, id_subcategory_subcategory,jobs.date_accesed
                        FROM (SELECT * FROM job_offer
                        	WHERE id_sector_main_sector = %s
                        	AND id_subcategory_subcategory = %s
                        	) as jobs LEFT JOIN
                        	(SELECT * FROM application
                        	WHERE id_customer_customer != %s) as apps
                        ON id_job = id_job_job_offer
                        ORDER BY id_job
                        ) as no_dups
                        ORDER BY no_dups.date_accesed DESC
                        LIMIT %s
                        """
            cursor.execute(sql_get, (id_sector,id_subcategory, id_customer, n_jobs))

        else:
            sql_get = """
                        SELECT *
                        FROM (
                        SELECT DISTINCT ON (id_job) id_job, name_job, description_job, email_job, id_company_company, id_sector_main_sector, id_subcategory_subcategory,jobs.date_accesed
                        FROM (SELECT * FROM job_offer
                        	WHERE id_sector_main_sector = %s
                        	) as jobs LEFT JOIN
                        	(SELECT * FROM application
                        	WHERE id_customer_customer != %s) as apps
                        ON id_job = id_job_job_offer
                        ORDER BY id_job
                        ) as no_dups
                        ORDER BY no_dups.date_accesed DESC
                        LIMIT %s
                        """
            cursor.execute(sql_get, (id_sector, id_customer, n_jobs))

        # MISSING INNER JOIN TO NOT REPEAT APPLYING TO A JOB OFFER.

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
t = get_jobs(1,4,None,100)
print(t)
print(len(t))
