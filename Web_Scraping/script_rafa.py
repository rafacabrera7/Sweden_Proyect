from selenium import webdriver
from progress.bar import Bar
import json
from time import sleep
import requests as r
from bs4 import BeautifulSoup


def get_all_urls(driver):
    cont = 0
    todos_los_empleos = []
    for j in range(1,1000):
        driver.get(f"https://arbetsformedlingen.se/platsbanken/annonser?page={j}&p=5:tPox_ie4_X9X&l=2:CifL_Rzy_Mku")
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


def get_info_job(driver, job):
    driver.get(job)
    title = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/h1").text
    empresa = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/h2").text
    try:
        correo = driver.find_element_by_xpath("/html/body/div[2]/div/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-jobb/div/section/div/div[2]/div[2]/aside[1]/div/pb-section-job-apply-component/div/div/div[2]/div/div[2]/span/a").text
    except:
        correo = "None"
    data = {"title":title,
            "entity":empresa,
            "email":correo,
            "url":job}
    return(data)


def get_full_info(driver):
    full_data = []
    urls = get_all_urls(driver)
    bar = Bar("progress" , max=len(urls))
    for i in urls:
        data = get_info_job(driver, i)
        full_data.append(data)
        bar.next()
    return(full_data)


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options = options)
all_i_need = get_full_info(driver)
with open("all_i_need_2.json" , "w") as file:
    json.dump(all_i_need , file)
    print("everyting done")
