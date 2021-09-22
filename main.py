import rss_reader
import json

from flask import Flask, redirect, request

app = Flask("__main__")


@app.route("/")
def inicio():
    return redirect("https://desafora2.libsyn.com")


@app.route("/api/episodios")
def episodios():
    episodios = rss_reader.desafora2_rss()

    if "desde" in request.args and "hasta" in request.args:
        desde = int(request.args["desde"])
        hasta = int(request.args["hasta"])

        result = episodios[desde:hasta]

        return json.dumps({ "episodios": result })

    return json.dumps({ "episodios": episodios })


if __name__ == "__main__":
    app.run(debug="True")
