#importo librerías necesarias
from selenium import webdriver
from progress.bar import Bar
import json
from time import sleep
import requests as r
from bs4 import BeautifulSoup

# orginal url: https://arbetsformedlingen.se/platsbanken/annonser?page={j}&p=5:tPox_ie4_X9X&l=2:CifL_Rzy_Mku
# test: https://arbetsformedlingen.se/platsbanken/annonser?page={j}&q=DISTRIBUTION

#this method gets an url and takes all the jobs in this link
def get_all_urls(driver ):
    cont = 0
    todos_los_empleos = []
    #idealmente quemar este numero (1000) no es muy buena practica, pero no podemos saber cuantas paginas hay, entonces establecemos un maximo de 1000 paginas (25.000) empleos
    for j in range(1,1000):
        driver.get(f"https://arbetsformedlingen.se/platsbanken/annonser?page={j}&p=5:tPox_ie4_X9X&l=2:CifL_Rzy_Mku")
        #esto espera 3 segundos a que cargue la pagina, si ya cargó , entonces ya no espera
        driver.implicitly_wait(3)
        for i in range(1,26):
            try:
                elemento = driver.find_element_by_xpath(f"/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/div[2]/pb-section-search-result/section/div[2]/div/div/div[2]/section/div[2]/pb-feature-search-result-card[{i}]/div/div[1]/h4/a")
                url = elemento.get_attribute("href")
                print(url, cont)
                todos_los_empleos.append(url)
                cont += 1
            except:
                return(todos_los_empleos)


#esta funcion recibe una url de una pagina de un trabajo y extrae los datos necesarios
def get_info_job(driver, job):
    ide = str(job)[-8:]
    driver.get(job)
    #estas partes lo que hacen es extraer los datos de los campos que están en la página
    title = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/h1").text
    empresa = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/h2").text
    description = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/div[1]/h3[1]").text
    #como a veces no existe el correo, si existe lo guardo y si no retorno que no existe
    try:
        correo = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/aside[1]/div/pb-section-job-apply-component/div/div/div[2]/div/div[2]/span/a").text
    except:
        correo = "None"
    #esto son los datos que estoy guardando como diccionario, luego los retorno
    data = {"title":title,
            "entity":empresa,
            "email":correo,
            "url":job,
            "id":ide,
            "description":description}
    return(data)


#esta funcion junta el proceso de las dos funciones anteriores
def get_full_info(driver):
    full_data = []
    #funcion que recolecta todas las urls
    urls = get_all_urls(driver)
    bar = Bar("progress" , max=len(urls))
    #por cada una de las urls extraigo los datos de estas
    for i in urls:
        data = get_info_job(driver, i)
        full_data.append(data)
        bar.next()
    return(full_data)


#estas lineas de codigo hace que el browser se ejecute en headless(no se vea)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

#esto abre el browser
driver = webdriver.Chrome(options = options)
all_i_need = get_full_info(driver)
#genero la lista en donde guardo todas las tuplas de python en la que recorro
#el diccionario que contiene la info(porque no se por que no usar el diccionario)
tuplas = []
for i in all_i_need:
    #extraigo los elementos del diccionario  y los guardo en la lista de tuplas
    element = (i["id"] , i["title"], i["description"] , i["entity"] , i["email"] , i["url"])
    tuplas.append(element)
    print(element)

#guardo el archivo json que a mi forma de ver es necesario, luego podría iterar
#sobre el json o hacer el query desde este script si quisiera
with open("all_i_need_3.json" , "w") as file:
    json.dump(all_i_need , file)
    print("everyting done")
