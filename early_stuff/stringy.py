
import random

name = ['Alex', 'Efecan', 'Grace']
greeting = [ 'welcome', 'sup', 'howdy', 'good afternoon']
space = ['\n', ' ', '\t']


def random_item( list ):
	item = list[random.randint(0, len(list)-1 )]
	return item

#random_item(greeting)
#random_item(name)







start = """
<html>
<head>
	<title>Homepage</title>
</head>

<body>
"""

end = """
</body>
</html>
"""
