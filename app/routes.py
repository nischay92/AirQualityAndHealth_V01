from flask import Blueprint, render_template

# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', title='Air Quality Dashboard')
#Base test for the code
@main.route('/statistics')
def statistics():
    return render_template('statistics.html')

@main.route('/geography')
def geography():
    return render_template('geography.html')
