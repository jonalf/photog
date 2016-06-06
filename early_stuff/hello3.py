import random
from flask import Flask, render_template
foo = Flask(__name__)

name = ['Alex', 'Efecan', 'Grace']
greeting = [ 'Welcome', 'Sup', 'Howdy', 'Good afternoon']

def random_item( list ):
	item = list[random.randint(0, len(list)-1 )]
	return item

@foo.route("/")
def hello():
	g = random_item(greeting) 
	n = random_item(name)
	return render_template('main.html', GREET = g, NAME = n )

if __name__ == "__main__":
    foo.run()