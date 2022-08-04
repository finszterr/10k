from google_apis import create_service
import last

CLIENT_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
]

service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

video_id = last.getLatestId() # My own video 'vs2X0VQkDZw'

# Example 1. Post A Comment
request_body = {
	'snippet': {
		'videoId': video_id,
		'topLevelComment': {
			'snippet': {
				'textOriginal': 'first'
			}
		}
	}
}

response = service.commentThreads().insert(
	part='snippet',
	body=request_body
).execute()

print(response)

print('commented')