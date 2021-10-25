import psycopg2
from connection import Connection

def insert_job_offer(tuple):
    # this function recieves one tuple and inserts the value corresponding to
    # name_job_offer in the table job_offer
    # since id_job_offer should be automatically generated, it returns that
    # id to be used later.
    # in case the job_offer has already been insert, it searches for its id
    # and returns it.
    try:
        con = psycopg2.connect(user = "postgres",
                               password = "Cabrera05",
                               database = "Sweden",
                               host = "localhost",
                               port = "5432")
        print("Conexión exitosa!")

        con.autocommit = False

        cursor = con.cursor()

        sql_check = """SELECT id_job_offer FROM job_offer"""
        cursor.execute(sql_check)
        job_offers_tuples = cursor.fetchall()
        job_offers_ls = []

        for job_offer in job_offers_tuples:
            job_offers_ls.append(job_offer[0])

        if tuple[0] not in job_offers_ls:
            

            sql_insert = """INSERT INTO job_offer VALUES (DEFAULT, %s)
                    RETURNING id_job_offer"""

            cursor.execute(sql_insert, (tuple[0],))
            print("Insertion completed!")

        else:
            sql_search = """SELECT id_job_offer FROM job_offer
                            WHERE name_job_offer = %s"""
            cursor.execute(sql_search,(tuple[0],))
            print("Value already existed")

        id_comp = cursor.fetchone()
        id_comp = id_comp[0]

        con.commit()

        return id_comp

    except psycopg2.Error as e:
        print("Error connecting", e)
        conexion.rollback();

    finally:
        cursor.close()
        con.close()
        print("Conection closed")
