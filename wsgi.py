from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    greeting = "Hello From Within Openshift"
    #greeting += os.environ["TEST_ENV"]
    print(greeting)
    return greeting



if __name__ == "__main__":
    application.run()
