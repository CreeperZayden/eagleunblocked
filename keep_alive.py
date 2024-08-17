from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the name.html template
    return render_template('eaglecraft.1.8.8.html')

# Function to run the Flask server
def keep_alive():
    # Run the app in the main thread
    app.run(host='0.0.0.0', port=5000, debug=True)
