from flask import Flask, request
from movies import models
import pandas as pd

app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/insert", methods=["GET"])
def insert():
    data = pd.read_csv("/src/movies/movie_results.csv")
    try:
        data.to_sql(con=models.engine, name="movies", if_exists="replace", index=False)
    except:
        print("error jeje")
    return "uwu", 200