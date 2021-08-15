from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>E ai MANO BROWN VERSÃO 2</h1>"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0',debug=True)
