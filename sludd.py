from flask import Flask
import json
import requests

app = Flask(__name__)

base_url = "https://wttr.in/sandvika?formatj1"

@app.get("/")
def rute_index():
    res = requests.get(base_url)
    data = res.json()
    akkuratt_naa = data["current_condition"][0]["temp_c"]
    return f"<h1>{akkuratt_naa}</h1>"

app.run(port=5000, debug=True)