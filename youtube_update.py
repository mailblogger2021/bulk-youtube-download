from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from time import sleep
import datetime

# Imported necessary libraries

CLIENT_SECRETS_FILE = 'youtube.json'
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# # Building the API
# flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
# credentials = flow.run_console()
# youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


# Building the API
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_local_server(port=0)  # Opens a local browser for OAuth authentication
youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def update_video(video_id):
    # Executing the request for video statistics
    request = youtube.videos().list(part="statistics", id=video_id)
    response = request.execute()
    response = response['items'][0]['statistics']

    # Creating new title
    data = {
        'views': response['viewCount'],
        'likes': response['likeCount'],
        'dislikes': response['dislikeCount'],
        'comments': response['dislikeCount']
    }

    title = f'This Video Has {data["views"]} Views, {data["likes"]} Likes, {data["dislikes"]} Dislikes and {data["comments"]} Comments as of {datetime.datetime.now().strftime("%d %b, %Y %I:%M %p")}'

    # Executing the request to update the title
    video_response = youtube.videos().list(id=video_id, part='snippet').execute()
    video_snippet = video_response['items'][0]['snippet']
    video_snippet['title'] = title
    video_update_response = youtube.videos().update(part='snippet', body=dict(snippet=video_snippet, id=video_id)).execute()

    # Printing the title
    print('The Updated Title is: ' + video_update_response['snippet']['title'])

if __name__ == '__main__':
    while True:
        try:
            update_video('VKuqU3MgtDE')
        except HttpError as e:
            print('An HTTP error {} occurred: {}'.format(e.resp.status, e.content))
        sleep(3600)  # Waiting to prevent reaching the quota maximum
