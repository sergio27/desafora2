import rss_reader
import json

from flask import Flask, render_template

app = Flask("__main__")


@app.get("/")
def inicio():
    episodios = rss_reader.desafora2_rss()

    return render_template("index.html", episodios=episodios[:20])


@app.get("/api/episodios")
def episodios():
    episodios = rss_reader.desafora2_rss()
    result = {
        "episodios": episodios
    }

    return json.dumps(result)


if __name__ == "__main__":
    app.run(debug="True")
