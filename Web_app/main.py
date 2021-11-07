# perform pip install fastapi[all]
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from typing import Optional
from pydantic import BaseModel


class Client(BaseModel):
    name: str
    email: str
    password: str


class ClientBodyInsert(BaseModel):
    id: int
    message_body_id: Optional[int] = None
    message_body: str


class JobOfferInsert(BaseModel):
    name: str
    description: str
    email_job_offer: str
    company: str
    city: str
    url: str
    main_category: str
    subcategory: str


class Application(BaseModel):
    client_id: int
    category: str
    subcategory: str
    number_toSend: int
    email_subject: str
    body_id: int
    cv_id: int


app = FastAPI()

app.mount("/web/static/", StaticFiles(directory="./web/static/"), name="static")


@app.get("/")
async def root():
    response = RedirectResponse(url='/web/static/index.html')
    # response = RedirectResponse(url='/web/static/login.html')
    return response


# @app.post("/login")
# async def onLogin():
#     # Manage Login Response, might need to modify parameters
#     response = RedirectResponse(url='/web/static/index.html')
#     return response


@app.get("/scrape/")
async def ScrapeRequest(
        city: str = "", main_category: str = "",
        subcategory: str = "", url=""):
    print(city)
    print(main_category)
    print(subcategory)
    print(url)
    return {"success": True, "msg": "Scrape Success/Error"}


@app.post("/insert_client")
async def insert_client(
        client: Client):
    # perform validations
    print(client.name)
    print(client.email)
    print(client.password)
    return {"success": True, "msg": "Inserted"}


@app.get("/list_clients")
async def list_clients():
    client1 = {"client_id": "1123", "name": "Pedrito",
               "email": "hello@gmail.com", "email_password": "mypassword123",
               "date_inserted": "19/29",
               "number_of_apps": "1111"}
    clients = [client1]
    count = len(clients)
    return {"success": True, "clients": clients, "count": count}


@app.get("/client_report/")
async def client_report(
    client_id: int,
    to_display: int,
):
    job1 = {"job_name": "Cleaner", "company": "notgoogle", "email": "cleaner@gmail.com",
            "url": "www.sample.com", "date": "some/format/youlike"}
    job2 = {"job_name": "Coder", "company": "prolly google", "email": "coder@gmail.com",
            "url": "www.notsample.com", "date": "9/11/2021"}

    jobs = [job1, job2]
    return {"success": True, "jobs": jobs, "max_applications": 10}


@app.get("/client_body_report/")
async def client_body_report(
    client_id: int
):
    body1 = {"id": "1245", "message_body": "very long message"}
    body2 = {"id": "123123", "message_body": "very long message body x2"}
    # please do include client id
    return {"success": True, "bodies": [body1, body2], "client_id": client_id}


@app.post("/client_insert_body")
async def client_insert_body(
    client: ClientBodyInsert
):
    if (client.message_body_id is None):
        print("editing existing message")
    print(client.id)
    print(client.message_body)

    return {"success": True, "msg": "Success Body Insert"}


@app.post("/insert_job_offer")
async def insert_joboffer(
    joboffer: JobOfferInsert
):
    print(joboffer.name)
    print(joboffer.email_job_offer)
    return {"success": True, "msg": "Successful JobOffer Insert"}


@app.get("/list_job_offer")
async def list_joboffer(
):
    joboff1 = {"job_name": "A very cool job",
               "description": "Need frontend stack", "company": "gululu",
               "url": "gululu.com", "date": "1900BC", "category": "Farming", "subcategory": "hello",
               "email_joboffer": "recruiter@gmail.com", "city": "Glasgow"}
    joboffers = [joboff1]
    return {"success": True, "msg": "Successful JobOffer Insert", "joboffers": joboffers}


@app.get("/list_jobcompanies")
async def list_jobcompanies():
    companies = {"1111": "Google", "222": "Amazon"}
    count = len(companies)
    return {"success": True, "companies": companies, "count": count}


@app.get("/company_report/")
async def company_report(
    company_id: int,
):
    job1 = {"job_name": "Cleaner", "company": "notgoogle", "url": "companyurl.com",
            "city": "California", "date": "some/format/youlike",
            "category": "Farming 2.0",
            "subcategory": "Cleaner Farming"}

    jobs = [job1]
    return {"success": True, "jobs": jobs}


@app.post("/apply")
async def apply_application(
        application: Application):
    # perform validations
    print(application.subcategory)
    print(application.body_id)
    print(application.client_id)

    return {"success": True, "msg": "applied good"}


@app.post("/uploadCV/")
async def uploadCV(
        client_id: int,
        cv_name: str,
        CVfile: UploadFile = File(None)):
    if CVfile is None:
        print("no cv given")
    else:
        print("received file bytes!")
        print(CVfile.filename)
    return {"msg": "upload worked ok i guess"}


@app.get("/cv_report/")
async def company_report(
    client_id: int,
):
    cv1 = {"id_cv": "1111", "cv_name": "coolcv.pdf?"}
    cv2 = {"id_cv": "2222", "cv_name": "coolercv.pdf?"}

    cvs = [cv1, cv2]
    return {"success": True, "cvs": cvs}
