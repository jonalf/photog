from flask import Flask
app = Flask(__name__)   #initializes your web program


def neato(x):
	return "!" * x


@app.route("/")  #function decorator it's tied to hello()
def hello():
    return "i'm sleepy"

@app.route("/mets")  #function decorator it's tied to mets()
def mets():
    return "Lets go mets" + neato(10)

if __name__ == "__main__":
	app.debug = True
	app.run()
