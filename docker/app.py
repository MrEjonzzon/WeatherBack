from flask import Flask, render_template, request
from weather_api import get_weather_data
from dotenv import load_dotenv

import os
import datetime

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Load API key from .env
load_dotenv()
api_key = os.getenv("API_KEY")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form input
        location = request.form.get("location")
        date = request.form.get("date")

        # Validate location
        if not location or (not any(c.isalpha() for c in location) and "," not in location):
            return render_template("index.html", error="Please enter a valid city name or coordinates.", location=location, date=date)

        # Validate date
        try:
            input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            if input_date < datetime.date(1950, 1, 1) or input_date > datetime.date.today():
                return render_template("index.html", error="Please enter a date between 1950 and today.", location=location, date=date)
        except (ValueError, TypeError):
            return render_template("index.html", error="Invalid date format.", location=location, date=date)

        # Fetch weather data from Visual Crossing API
        weather = get_weather_data(api_key, location, date)

        # Handle error
        if not weather:
            return render_template("index.html", error="Weather data not found.", location=location, date=date)

        return render_template("index.html", weather=weather, location=location, date=date)
    
    else:
        # User reached route via GET (as by clicking a link or via redirect)
        return render_template("index.html")