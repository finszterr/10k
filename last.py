from regex import R
from google_apis import create_service

CLIENT_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
]

service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

playlist_id = 'UUX6OQ3DkcsbYNE6H8uQQuVA'

# Get latest video
response = service.playlistItems().list(
        part="snippet",
        maxResults=1,
        playlistId="UUX6OQ3DkcsbYNE6H8uQQuVA"
    )
lastShortId = 'aaa' #'dZklZVaU4AI'
for i in range(10):
	r = response.execute()
	r = r['items'][0]['snippet']['resourceId']['videoId']
	if(r != lastShortId):
		print(r)
		break