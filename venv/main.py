""" A microservice that will provide the current Unix time, or epoch time."""
import os
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_time():
    """ Retrieves and displays the epoch time. """
    return str(int(time.time()))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host="0.0.0.0", port=port, debug=True)