import random
from flask import Flask
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
	page = "<html><head><title>Hola</title></head><body><center><h1>"
	page = page + random_item(greeting) + ' ' + name
	page = page + "</h1></center></body></html>"
	return page

if __name__ == "__main__":
	foo.debug = True
	foo.run(port=9001)