"""the web api handler"""
# system lib tools
import os

# the flask web controller
import flask

# xray middleware and controller
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# the classic app router
app = flask.Flask(__name__)

# xray mdlw
xray_recorder.configure(service="entry API")
XRayMiddleware(app, xray_recorder)

# import the libraries that controls the downstream calls
import boto3
import requests

from aws_xray_sdk.core import patch_all
patch_all()

@app.route("/users/all", methods=["GET"])
def get_all_name():
    requests.get("https://blog.matthew-cloud.com/")
    return str(query_all_users())

def query_all_users():
    """query all users in a ddb table via a scan"""
    ddb = boto3.resource("dynamodb")
    tb = ddb.Table(os.environ.get("TABLE_NAME"))
    return tb.scan()