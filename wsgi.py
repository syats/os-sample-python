from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    greeting = "Hello From Within Openshift \n "
    #greeting += os.environ["TEST_ENV"]

    # config_file = "/configFiles/my-config-file"
    # f = open(config_file,"rt")
    # config_string = f.read()
    # greeting += config_string.strip()


    print(greeting)
    return greeting



if __name__ == "__main__":
    application.run()
