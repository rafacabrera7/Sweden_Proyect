import psycopg2
from datetime import date
from dbSQL import *

t = get_jobs(1,100, 4,3)
print(t)
print(len(t))
