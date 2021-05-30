from server.routes.compliment import router as complimentRouter
from dotenv import load_dotenv
from bson.json_util import dumps
from server.database import *
from server.models.compliment import complimentSchema
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
import random
import requests
import pymongo
import json
import re
import os

load_dotenv()

app = FastAPI()

app.include_router(complimentRouter, tags=["Controller"], prefix="/Controller")

@app.get("/", tags=["Root"])
def hello():
    return {"Hello":"World"}

@app.get("/compliment/", tags=["Compliments"])
async def get_compliment(language:str = 'portugues', compliment_number:int = 1):
    numbers = []
    results = []
    cur.execute(f"SELECT * from compliments WHERE language = '{language}'")
    fetch = cur.fetchall()

    if len(fetch) < compliment_number:
        return {"message":"Voce solicitou um numero de frases maior do que as disponiveis no nosso banco de dados"}
    else:
        for i in range(compliment_number):
            print(i)
            print(len(fetch))
            number = random.randint(0,len(fetch)-1)
            print(number)
            
            while number in numbers:
                print('entering while')
                number = random.randint(0,len(fetch)-1)
            numbers.append(number)

        numbers.sort()

        for x in numbers:results.append({fetch[x][0]:{'text':fetch[x][1],'language':fetch[x][2]}})

        return results

@app.post("/compliment/add/",tags=["Compliments"])
async def add_compliment(compliment: complimentSchema):
    try:
        compliment = jsonable_encoder(compliment)
        print(compliment)
        print(compliment['text'])
        cur.execute(f"INSERT INTO compliments (text,language) VALUES ('{compliment['text']}','{compliment['language']}')")
        client.commit()
        print("commitando insert")
        print("fazendo select")
        cur.execute(f"SELECT * from compliments WHERE id = {cur.lastrowid}")
        print("fazendo fetch")
        new_compliment = cur.fetchone()
        print("retornando")
        return [{"values":{"id":new_compliment[0],"text":new_compliment[1],"language":new_compliment[2]}},{"message":"Valores inseridos no banco"}]
    except Exception as e:
        print(e)
        return {"message":"Nao foi passado valores corretamente"}

@app.on_event("shutdown")
def shutdown_event():
    print("connection closed")
    client.close()