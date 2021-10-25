import psycopg2
from connection import Connection

#tuple will be like: (i["id"] , i["title"], i["description"], i["email"] , i["entity"], date_accesed , i["url"], city, main_sector, subcategory)

def insert_company(tuple):
    # this function recieves one tuple and inserts the value corresponding to
    # name_company in the table company
    # since id_company should be automatically generated, it returns that
    # id to be used later.
    # in case the company has already been insert, it searches for its id
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

        sql_check = """SELECT name_company FROM company"""
        cursor.execute(sql_check)
        companies_tuples = cursor.fetchall()
        companies_ls = []

        for company in companies_tuples:
            companies_ls.append(company[0])

        if tuple[0] not in companies_ls:
            sql_insert = """INSERT INTO company VALUES (DEFAULT, %s)
                    RETURNING id_company"""

            cursor.execute(sql_insert, (tuple[0],))
            print("Insertion completed!")

        else:
            sql_search = """SELECT id_company FROM company
                            WHERE name_company = %s"""
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

def insert_city(tuple):
    # this function recieves one tuple and inserts the value corresponding to
    # name_city in the table city
    # since id_city should be automatically generated, it returns that
    # id to be used later.
    # in case the city has already been insert, it searches for its id
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

        sql_check = """SELECT name_city FROM city"""
        cursor.execute(sql_check)
        cities_tuples = cursor.fetchall()
        cities_ls = []

        for city in cities_tuples:
            cities_ls.append(city[0])

        if tuple[0] not in cities_ls:
            sql_insert = """INSERT INTO city VALUES (DEFAULT, %s)
                    RETURNING id_city"""

            cursor.execute(sql_insert, (tuple[0],))
            print("Insertion completed!")

        else:
            sql_search = """SELECT id_city FROM city
                            WHERE name_city = %s"""
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

def insert_sector(tuple):
    # this function recieves one tuple and inserts the value corresponding to
    # name_sector in the table sector
    # since id_sector should be automatically generated, it returns that
    # id to be used later.
    # in case the sector has already been insert, it searches for its id
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

        sql_check = """SELECT name_sector FROM main_sector"""
        cursor.execute(sql_check)
        sectors_tuples = cursor.fetchall()
        sectors_ls = []

        for sector in sectors_tuples:
            sectors_ls.append(sector[0])

        if tuple[0] not in sectors_ls:
            sql_insert = """INSERT INTO main_sector VALUES (DEFAULT, %s)
                    RETURNING id_sector"""

            cursor.execute(sql_insert, (tuple[0],))
            print("Insertion completed!")

        else:
            sql_search = """SELECT id_sector FROM main_sector
                            WHERE name_sector = %s"""
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

def insert_subcategory(tuple):
    # this function recieves one tuple and inserts the value corresponding to
    # name_subcategory in the table subcategory
    # since id_subcategory should be automatically generated, it returns that
    # id to be used later.
    # in case the subcategory has already been insert, it searches for its id
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

        sql_check = """SELECT name_subcategory FROM subcategory"""
        cursor.execute(sql_check)
        subcategories_tuples = cursor.fetchall()
        subcategories_ls = []

        for subcategory in subcategories_tuples:
            subcategories_ls.append(subcategory[0])

        if tuple[0] not in subcategories_ls:
            sql_insert = """INSERT INTO subcategory VALUES (DEFAULT, %s)
                    RETURNING id_subcategory"""

            cursor.execute(sql_insert, (tuple[0],))
            print("Insertion completed!")

        else:
            sql_search = """SELECT id_subcategory FROM subcategory
                            WHERE name_subcategory = %s"""
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
