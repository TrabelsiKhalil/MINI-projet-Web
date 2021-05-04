from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


import mysql.connector

import urllib.parse
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Game(BaseModel):
    id: Optional[int] = 0
    title: Optional[str] = ""
    progres: Optional[int] = 0
    status_id: Optional[int]
    status_name: Optional[str] = ""
    img_url: Optional[str] = ""


@app.get("/game/get/")
def get_all_games():
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="GAMEARCHIVE")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM jeux")
    row_headers=[x[0] for x in mycursor.description]
    result = mycursor.fetchall() 
    if result:
        res_dict = [dict(zip(row_headers,el)) for el in result]  # wrap res in dict with cursor/table headers
        games = []
        for game in res_dict:
            _id = game["status_id"]
            mycursor.execute(f"SELECT title FROM status where id={_id}")
            game["status_name"] = mycursor.fetchone()[0]
            games.append(game)
        return games
    return result

@app.post("/game/add/")
def add_game(game: Game):
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="GAMEARCHIVE")
    mycursor = mydb.cursor()

    game_data = game.dict()

    # add the image
    img_url = get_game_img(game_data["title"])


    insert_stmt = f"INSERT INTO jeux(title,progres,status_id,img_url) VALUES ('{game_data['title']}',{game_data['progres']},{game_data['status_id']},'{img_url}')"
    mycursor.execute(insert_stmt)
    mydb.commit()
   
    return dict(game, **{"img_url":img_url})

# @app.get("/game/get/{_id}")
# def find_game_by_id(_id:int):
#     mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="GAMEARCHIVE")
#     mycursor = mydb.cursor()
#     mycursor.execute(f"SELECT * FROM jeux WHERE id = {_id}")
#     row_headers=[x[0] for x in mycursor.description]
#     result = mycursor.fetchone()
#     if result:
#         return dict(zip(row_headers,result)) # wrap res in dict with cursor/table headers
#     return {}


@app.get("/game/search/{title}")
def find_game_by_title(title:str):
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="GAMEARCHIVE")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM jeux WHERE title like  '%{title}%'")
    # return mycursor.fetchone()
    row_headers=[x[0] for x in mycursor.description]
    result = mycursor.fetchall()
    if result:
        return  [dict(zip(row_headers,el)) for el in result]  # wrap res in dict with cursor/table headers
    return {}
   


@app.delete("/game/delete/{_id}")
def delete_game(_id:int):
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="GAMEARCHIVE")
    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM jeux where id = {_id} ")
    mydb.commit()
    return {}



@app.put("/game/update/")
def update_game(game: Game):
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="GAMEARCHIVE")
    mycursor = mydb.cursor()
    insert_stmt = "UPDATE jeux SET title = %(title)s, progres = %(progres)s,status_id = %(status_id)s WHERE id = %(id)s"
    mycursor.execute(insert_stmt, game.dict())
    mydb.commit()
    game_data = game.dict()
    mycursor.execute(f"SELECT title FROM status where id={game_data['status_id']}")
    return dict(game, **{"status_name":mycursor.fetchone()[0]})



# api 2

headers = {
    'Accept': '*/*',
    'Access-Control-Allow-Origin': '*' ,
    'Client-ID': 'l756m3rkdkgov1xpqlxfyjlrspof6t',
    'Authorization': 'Bearer vlcsaaabi8mqgvavovsba4oxbq8cpl'
}

params = {
    "name":"",
    "status":"",
    "screenshots":"url",
    "cover":"url",
    "platforms":"name",
    "genres":"name",
    "summary":"",
    "storyline":"",
    "total_rating":"",
    "total_rating_count":"",
    "rating":"",
    "rating_count":"",
    "release_dates":"human",
    "artworks":"url",
    "videos":"*",
    "storyline":""
}


def parm_parser(main,fields):
    req = main + "&fields="
    for item in fields.items():
        if item[1] == "":
            req += item[0] + ","
        else:
            req += "{}.{}".format(item[0],item[1]) + ","
    return req[:-1]

def checkKey(dict, key):      
    if key in dict.keys(): 
        return True
    else: 
        return False


def fix_urls(url):
    url = url.replace("t_thumb", "t_original")
    url = url.replace("//","http://")
    return url

def fix_videos(id):
    return "https://www.youtube.com/embed/{}?controls=0&modestbranding=1&rel=0&showinfo=0&loop=0&fs=0&hl=en&iv_load_policy=3&enablejsapi=1".format(id)

def parse_json(res):
    data = {}
    try:
        for item in res[0].items():
            if isinstance(item[1], list): 
                # data[item[0]] =
                temp_arr = []
                found = False
                if checkKey(item[1][0],"name") and found == False:
                    keyword = "name"
                    found = True
                if checkKey(item[1][0],"url") and found == False:
                    keyword = "url" 
                    found = True
                if checkKey(item[1][0],"video_id") and found == True:
                    keyword = "video_id" 
                    found = True
                if found == False:
                    keyword = "human" 

                for el in item[1]:
                    if keyword == "url":
                        temp_arr.append(fix_urls(el[keyword]))
                    elif keyword == "video_id":
                        temp_arr.append(fix_videos(el[keyword]))
                    else:
                        temp_arr.append(el[keyword])
                data[item[0]] = temp_arr

            elif isinstance(item[1], dict):
                if item[0] == "cover":
                    data[item[0]] = {"url":fix_urls(item[1]["url"])}
            else:
                data[item[0]] = item[1]
    except:
        pass
    return data



def get_game_img(title):
    img_params = {
    "cover":"url",
    }
    title = urllib.parse.unquote(title)
    r = requests.post("https://api.igdb.com/v4/games/?search={}&limit=1".format(parm_parser(title,img_params)),headers=headers)
    res = r.json()
    return parse_json(res)["cover"]["url"]

@app.get("/game/info")
async def get_info(title:str):
    title = urllib.parse.unquote(title)
    r = requests.post("https://api.igdb.com/v4/games/?search={}&limit=1".format(parm_parser(title,params)),headers=headers)
    res = r.json()
    return parse_json(res)










