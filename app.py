from flask import Flask, jsonify, request
from api.index import handler as index_handler  # Import function for the index route
from api.transcripts.common import handler as common_handler  # Import function for /transcripts/common
from api.transcripts.overlap import handler as overlap_handler  # Import function for /transcripts/overlap

app = Flask(__name__)

# Define routes for each of your serverless functions
@app.route("/", methods=["GET"])
def index():
    return index_handler(request)

@app.route("/transcripts/common", methods=["GET"])
def common():
    return common_handler(request)

@app.route("/transcripts/overlap", methods=["GET"])
def overlap():
    return overlap_handler(request)

# Run the Flask app if this script is executed
if __name__ == "__main__":
    app.run(debug=True)

