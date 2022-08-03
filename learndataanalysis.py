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

video_id = 'vs2X0VQkDZw'

# Example 1. Post A Comment
request_body = {
	'snippet': {
		'videoId': video_id,
		'topLevelComment': {
			'snippet': {
				'textOriginal': 'BC'
			}
		}
	}
}

response = service.commentThreads().insert(
	part='snippet',
	body=request_body
).execute()

print(response)


# # Example 2. Reply To A Comment
# comment_id = '<comment id>'
# request_body = {
# 	'snippet': {
# 		'parentId': comment_id,
# 		'textOriginal': 'Hello'
# 	}
# }

response = service.comments().insert(
	part='snippet',
	body=request_body
).execute()