from flask import Flask, render_template
from threading import Thread

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render the HTML template
    return render_template('name.html')

# Function to run the Flask app
def run():
    # Run the Flask app with debug mode enabled for detailed error logs
    app.run(host='0.0.0.0', port=8080, debug=True)

# Function to keep the server alive by running it in a separate thread
def keep_alive():
    # Create and start a new thread to run the Flask app
    t = Thread(target=run)
    t.start()
