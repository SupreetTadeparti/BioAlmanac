import json
from flask import Flask, render_template

app = Flask(__name__)

f = open("data.json", "r")
data = json.load(f)
f.close()

categories = ["Endangered", "Critically Endangered", "Extinct in the Wild"]

plant_data = {
    category : [plant for plant  in data["Plants"] if plant["endangerment_status"] == category] 
    for category in categories
}

animal_data = {
    category : [animal for animal  in data["Animals"] if animal["endangerment_status"] == category] 
    for category in categories
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/plant-almanac")
def plant_almanac():
    return render_template("plant_almanac.html", data=plant_data)

@app.route("/animal-almanac")
def animal_almanac():
    return render_template("animal_almanac.html", data=animal_data)

@app.route("/plant/<plant_name>")
def plant(plant_name):
    return render_template("plant.html", plant=[plant for plant in data["Plants"] if plant["name"] == plant_name.replace("-", " ")][0])

@app.route("/animal/<animal_name>")
def animal(animal_name):
    return render_template("animal.html", animal=[animal for animal in data["Animals"] if animal["name"] == animal_name.replace("-", " ")][0])

if __name__ == "__main__":
    app.run(debug=True, port=3000)