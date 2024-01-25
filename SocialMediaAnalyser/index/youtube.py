import googleapiclient.discovery
import os

def main(id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyApEGHh85RNpHTrV22I1TW_36Z-Q7T24Pc"


    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=id,
    )
    response = request.execute()
    response = response['items']
    comments_list = []

    for x in response:
        comments = x["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments_list.append(comments)
    
    return(comments_list)