#Coded by Eddie's Tech (eddiestech.co.uk) - Adapted from YouTube API example
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
import ctypes
import admin

def main():
    print(ctypes.windll.shell32.IsUserAnAdmin())
    rc = 0
    if not admin.isUserAdmin():
        print("You're not an admin.", os.getpid(), "params: ", sys.argv)
        rc = admin.runAsAdmin()
    else:
        print("You are an admin!", os.getpid(), "params: ", sys.argv)
        rc = 0
    #input('Press Enter to exit.')
    #return rc
    admin.runAsAdmin('print a')

    channel = 'InterestingExplained' #input('Channel id: ')
    video = 'vs2X0VQkDZw' #input('Video id: ')
    commenttext = 'aaa' #input('Comment text: ')
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "channelId": channel,
                "videoId": video,
                "topLevelComment": {
                    "snippet":{
                        "textOriginal": commenttext
                        }
                    }
                }
            }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()