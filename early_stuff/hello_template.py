import random
from flask import Flask, render_template

foo = Flask(__name__)

names = ['Alex', 'Efecan', 'Grace']
greeting = [ 'Welcome', 'Sup', 'Howdy', 'Good afternoon']

def random_item( list ):
	item = list[random.randint(0, len(list)-1 )]
	return item

@foo.route("/")
@foo.route("/<name>")
def hello(name=None):
	if not name:
		name = random_item(names)
	greet = random_item( greeting )
	return render_template( "base.html", GREETING = greet, PERSON = name )

if __name__ == "__main__":
	foo.debug = True
	foo.run(port=9001)