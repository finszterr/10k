from google_apis import create_service
import time

def getLatestId():
	CLIENT_FILE = 'client_secret.json'
	API_NAME = 'youtube'
	API_VERSION = 'v3'
	SCOPES = [
		'https://www.googleapis.com/auth/youtube',
		'https://www.googleapis.com/auth/youtube.force-ssl',
		'https://www.googleapis.com/auth/youtubepartner'
	]

	service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

	# Get latest video of Uploads playlist -> MrBeasts: UUX6OQ3DkcsbYNE6H8uQQuVA
	response = service.playlistItems().list(
			part="snippet",
			maxResults=1,
			playlistId="UUX6OQ3DkcsbYNE6H8uQQuVA"
		)
	lastShortId = 'dZklZVaU4AI' # Last Mr Beasts short id: 'dZklZVaU4AI'
	#while True:
	#for _ in range(1):
	while True:
		r = response.execute()
		r = r['items'][0]['snippet']['resourceId']['videoId']
		if(r != lastShortId):
			print(r)
			break
		print('No')
	
	return r