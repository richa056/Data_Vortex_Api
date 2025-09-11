from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

def load(path):
    """Helper function to read CSV and convert to JSON records"""
    return pd.read_csv(path).to_dict(orient="records")

@app.route("/health")
def health():
    return {"status": "ok"}


# ----------------------- ROUND-1 -----------------------
@app.route("/round1/earth_planet")
def round1_earth_planet():
    return jsonify(load("data/round1_earth_planet.csv"))

@app.route("/round1/earth_resources")
def round1_earth_resources():
    return jsonify(load("data/round1_earth_resources.csv"))

@app.route("/round1/earth_climate")
def round1_earth_climate():
    return jsonify(load("data/round1_earth_climate.csv"))

@app.route("/round1/earth_soil")
def round1_earth_soil():
    return jsonify(load("data/round1_earth_soil.csv"))


# ----------------------- ROUND-2 -----------------------
@app.route("/round2/planets")
def round2_planets():
    return jsonify(load("data/round2_planets.csv"))

@app.route("/round2/climate")
def round2_climate():
    return jsonify(load("data/round2_climate.csv"))

@app.route("/round2/soil")
def round2_soil():
    return jsonify(load("data/round2_soil.csv"))

@app.route("/round2/resources")
def round2_resources():
    return jsonify(load("data/round2_resources.csv"))

@app.route("/round2/habitability_scores")
def round2_habitability_scores():
    return jsonify(load("data/habitability_scores.csv"))

@app.route("/round2/colonization_history")
def round2_colonization_history():
    return jsonify(load("data/colonization_history.csv"))

# New endpoints added in Round-2
@app.route("/round2/biosphere")
def round2_biosphere():
    return jsonify(load("data/biosphere.csv"))

@app.route("/round2/energy_sources")
def round2_energy_sources():
    return jsonify(load("data/energy_sources.csv"))


# ----------------------- ROUND-3 (Crisis) -----------------------
@app.route("/round3/planets")
def round3_planets():
    return jsonify(load("data/round2_planets.csv"))

@app.route("/round3/climate")
def round3_climate():
    return jsonify(load("data/round2_climate.csv"))

@app.route("/round3/soil")
def round3_soil():
    return jsonify(load("data/round2_soil.csv"))

@app.route("/round3/resources")
def round3_resources():
    # Endpoint deliberately disabled in crisis mode
    return jsonify({"error": "Endpoint unavailable in crisis"}), 404


@app.route("/round3/habitability_scores")
def round3_habitability_scores():
    return jsonify(load("data/habitability_scores.csv"))

@app.route("/round3/colonization_history")
def round3_colonization_history():
    return jsonify(load("data/colonization_history.csv"))

@app.route("/round3/biosphere")
def round3_biosphere():
    return jsonify(load("data/biosphere.csv"))

@app.route("/round3/energy_sources")
def round3_energy_sources():
    return jsonify(load("data/energy_sources.csv"))


if __name__ == "__main__":
    # host="0.0.0.0" is required for Render deployment
    app.run(host="0.0.0.0", port=5000)
