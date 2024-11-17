from flask import Blueprint, render_template, request, jsonify
from . import db
from .enums import Pollutants, IndianaCounty
from .models import AirQualityData
import pandas as pd
from sqlalchemy.sql import func
# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', title='Air Quality Dashboard')
#Base test for the code
@main.route('/statistics')
def statistics():
    return render_template('statistics.html',pollutants = Pollutants, countys = IndianaCounty)


@main.route('/geography')
def geography():
    return render_template('geography.html')

@main.route('/search', methods=['GET'])
def search():
    # Extract query parameters from the form
    data = pd.read_csv("/Users/nischay92/Documents/IUBCourse/LuddyHacks16Nov/AirQualityAndHealth_V01/AirData.csv")

    pollutant = request.args.get('pollutant')
    county = request.args.get('county')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Filter the data
    filtered_data = data[
        (data['pollutants'] == pollutant) &
        (data['county'] == county) &
        (data['date_local'] >= start_date) &
        (data['date_local'] <= end_date)
    ]

    # Convert filtered data to list of dictionaries
    results = filtered_data.to_dict(orient='records')

    # If it's an AJAX request, return JSON data
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(results)

    # Otherwise, render the results page
    return render_template('/PartialPages/results.html', results=results)