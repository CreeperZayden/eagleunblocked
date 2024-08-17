from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Raw GitHub URL for the HTML file
    url = "https://raw.githubusercontent.com/CreeperZayden/eagleunblocked/main/eaglercraft.1.8.8.html"
    
    # Fetch the HTML content from GitHub
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Serve the HTML content
        return Response(response.text, mimetype='text/html')
    else:
        # Handle the case where the file couldn't be fetched
        return "Failed to fetch the HTML content.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
