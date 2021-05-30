import sqlite3
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

load_dotenv()

client = sqlite3.connect('server/database.db')
cur = client.cursor()


def compliment_helper(compliment) -> dict:
    return {
        "title":  compliment["title"],
        "language": compliment["language"]
    }

async def retrieve_compliments():
    compliments = []
    cur.execute("SELECT * from compliments")
    async for compliment in cur.fetchall():
        compliments.append(compliment_helper(compliment))
    return compliments


# Add a new compliment into to the database
async def add_compliment(compliment_data: dict) -> dict:
    cur.execute(f"INSERT INTO compliments VALUES ('{compliment_data[0]['text']}','{compliment_data[0]['language']}')")
    client.commit()
    cur.execute(f"SELECT * from compliments WHERE id = {cur.lastrowid}")
    new_compliment = await cur.fetchone()
    return compliment_helper(new_compliment)


# Retrieve a compliment with a matching ID
async def retrieve_compliment(id: int) -> dict:
    cur.execute(f"SELECT * from compliments WHERE id = {id}")
    compliment = await cur.fetchone()
    if compliment:
        return compliment_helper(compliment)


# Update a compliment with a matching ID
async def update_compliment(id: int, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    cur.execute(f"SELECT * from compliments WHERE id = {id}")
    compliment = await cur.fetchone()
    if compliment:
        sql_update_query = f"""UPDATE compliments set text = '{data[0]['text']}', language = '{data[0]['language']}' where id = {id}"""
        updated_compliment = cur.execute(sql_update_query)
        if updated_compliment:
            client.commit()
            return True
        return False


# Delete a compliment from the database
async def delete_compliment(id: int):
    cur.execute(f"SELECT * from compliments WHERE id = {id}")
    compliment = await cur.fetchone()
    if compliment:
        await cur.execute(f"DELETE FROM compliments WHERE id = {id}")
        client.commit()
        return True