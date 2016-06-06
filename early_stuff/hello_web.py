from flask import Flask
import random

app = Flask(__name__)

name = ['Alex', 'Efecan', 'Grace']
greeting = [ 'welcome', 'sup', 'howdy', 'good afternoon']

def random_item( list ):
    return list[ random.randint(0, len(list) - 1 )]

@app.route("/")
def hello():
    line = random_item( greeting )
    line = line +'<h3>'
    line+= random_item( name )
    line+= '</h3>'
    return line

if __name__ == "__main__":
	app.debug = True
	app.run()
