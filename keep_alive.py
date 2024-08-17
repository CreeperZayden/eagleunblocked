from flask import Flask, render_template
from threading import Thread

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the name.html template
    return render_template('eaglecraft.1.8.8.html')

# Function to run the Flask server
def run():
    # Run the app with debug mode enabled on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

# Function to keep the Flask server running in the background
def keep_alive():
    # Start the server in a new thread
    t = Thread(target=run)
    t.start()
