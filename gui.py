import requests
import gui

url = 'https://api.nasa.gov/planetary/apod/'

arg = {'api_key': '1IxVttZyP7rV2jQFrl6EkfT9wa6NIn13XWw2KTJL'}

response = requests.get(url, params=arg)

if response.status_code == 200:
	document = response.json()

	if 'copyright' in document:
		gui.gui(document['title'], document['explanation'], document['url'], copyright=document['copyright'])
	else:
		gui.gui(document['title'], document['explanation'], document['url'])

else:
	print(response.content)