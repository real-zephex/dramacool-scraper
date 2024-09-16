from flask import Flask, jsonify, request
from src.popular import Popular
from src.recent import Recent
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")
def welcome():
    return (
        jsonify(
            {
                "message": "Welcome. This scrapers scrapes the list of popular kdramas from dramacool"
            }
        )
    )
    
@app.route("/popular")
@cache.cached(timeout=300)
def popular():
    page = request.args.get("page")
    if page:
        pass
    else: page = "1"
    return jsonify(Popular(page).fetch_data())

@app.route("/recent")
@cache.cached(timeout=300)
def recent():
    return jsonify(Recent().fetch_data())

if __name__ == "__main__":
    app.run(debug=True)