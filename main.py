import os
import json
import datetime
from flask import Flask

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER,"resourses")

@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_DIR,"response.json")) as f:
        return "%s - %s" % (json.loads(f.read()).get("message"),datetime.datetime.now())

if __name__ == "__main__":
                            app.run(host="0.0.0.0",port="8080",debug="true")
