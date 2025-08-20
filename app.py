from flask import Flask, jsonify
import pandas as pd

# ⚠️ CHANGE THIS DURING THE EVENT:
# 1 = Round-1 (Earth data only)
# 2 = Round-2 (Planet modelling dataset)
# 3 = Round-3 (Crisis mode)
CURRENT_ROUND = 1

app = Flask(__name__)

def load(path):
    return pd.read_csv(path).to_dict(orient="records")

@app.route("/health")
def health():
    return {"status": "ok"}

# ----------------------- ROUND-1 : Earth only -----------------------
@app.route("/earth_planet")
def earth_planet():
    if CURRENT_ROUND == 1:
        return jsonify(load("data/round1_earth_planet.csv"))
    return jsonify({"error":"Only available in Round-1"}), 404

@app.route("/earth_resources")
def earth_resources():
    if CURRENT_ROUND == 1:
        return jsonify(load("data/round1_earth_resources.csv"))
    return jsonify({"error":"Only available in Round-1"}), 404

@app.route("/earth_climate")
def earth_climate():
    if CURRENT_ROUND == 1:
        return jsonify(load("data/round1_earth_climate.csv"))
    return jsonify({"error":"Only available in Round-1"}), 404

@app.route("/earth_soil")
def earth_soil():
    if CURRENT_ROUND == 1:
        return jsonify(load("data/round1_earth_soil.csv"))
    return jsonify({"error":"Only available in Round-1"}), 404



# --------------------- ROUND-2 + ROUND-3  PLANETS DATA ---------------------

@app.route("/planets")
def planets():
    if CURRENT_ROUND >= 2:
        return jsonify(load("data/round2_planets.csv"))
    return jsonify({"error": "Not available in Round-1"}), 404

@app.route("/climate")
def climate():
    if CURRENT_ROUND >= 2:
        return jsonify(load("data/round2_climate.csv"))
    return jsonify({"error": "Not available in Round-1"}), 404

@app.route("/soil")
def soil():
    if CURRENT_ROUND >= 2:
        return jsonify(load("data/round2_soil.csv"))
    return jsonify({"error": "Not available in Round-1"}), 404

@app.route("/resources")
def resources():
    # -> available during Round-2
    if CURRENT_ROUND == 2:
        return jsonify(load("data/round2_resources.csv"))
    # -> removed during crisis (Round-3)
    if CURRENT_ROUND == 3:
        return jsonify({"error":"Endpoint unavailable in crisis"}),404
    return jsonify({"error":"Not available in Round-1"}),404

@app.route("/habitability_scores")
def habitability_scores():
    if CURRENT_ROUND >= 2:
        return jsonify(load("data/habitability_scores.csv"))
    return jsonify({"error":"Not available in Round-1"}),404

@app.route("/colonization_history")
def colonization_history():
    if CURRENT_ROUND >= 2:
        return jsonify(load("data/colonization_history.csv"))
    return jsonify({"error":"Not available in Round-1"}),404


# --------------------  ROUND-3 only (new endpoints) -------------------------
@app.route("/biosphere")
def biosphere():
    if CURRENT_ROUND == 3:
        return jsonify(load("data/biosphere.csv"))
    return jsonify({"error":"Not available until crisis round"}),404

@app.route("/energy_sources")
def energy_sources():
    if CURRENT_ROUND == 3:
        return jsonify(load("data/energy_sources.csv"))
    return jsonify({"error":"Not available until crisis round"}),404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
