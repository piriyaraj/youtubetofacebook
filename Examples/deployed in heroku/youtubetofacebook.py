from fileinput import filename
from os.path import exists
import os
from this import d
import time
from unittest import result
from urllib import request, response
import pytube
from pytube import YouTube
import scrapetube
import requests


class youtubetofb:
    newVideosData = []
    downloadedVideoPath = []
    downloadedVideoTitle = []
    downloadedVideoThumbnails = []
    lastVideoId = ''

    def __init__(self, youtubeLink, facebookApi, pageId):
        self.youtubeLink = youtubeLink
        self.facebookApi = facebookApi
        self.facebookId = pageId

    def haveNewVideo(self, lastPostId=""):
        """check if any new video available"""
        try:
            file = open("log.txt", 'r')
        except:
            open("log.txt", 'w').close()
            file = open("log.txt", 'r')
        if(lastPostId == ""):
            lastPostId = file.readline()
        else:
            print("you send the last video ", lastPostId)
        file.close()
        channelId = pytube.contrib.channel.Channel(self.youtubeLink).channel_id
        videos = scrapetube.get_channel(channelId)
        count = 1
        for video in videos:
            if(lastPostId == video['videoId']):
                break
            if(count == 1):
                count += 1
                open("log.txt", 'w').write(video['videoId'])
                lastVideoId = video['videoId']
            self.newVideosData.append(video)
        if(len(self.newVideosData) > 0):
            return True, lastVideoId
        else:
            return False

        pass

    def downloadVideo(self):
        count = 1
        for video in self.newVideosData:
            videoId = video['videoId']
            yt = YouTube("https://www.youtube.com/watch?v="+videoId)
            filename = "Dont Be Corner "+str(count)+".mp4"
            yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download(filename=filename)
            # videoThumbnailUrl = video['thumbnail']['thumbnails'][-1]['url']
            videoTitle = video['title']['runs'][0]['text']
            # file = open(videoTitle+".png", "wb")
            # response=requests.get(videoThumbnailUrl)
            # file.write(response.content)
            # file.close()
            # newName = os.path.abspath(videoTitle+".mp4").replace(videoTitle,str(count))
            # os.rename(os.path.abspath(videoTitle+".mp4"), newName)
            self.downloadedVideoTitle.append(videoTitle)
            self.downloadedVideoPath.append("./"+filename)

            count += 1
            # self.downloadedVideoThumbnails.append(os.path.abspath(videoTitle+".png"))
        pass

    def postVideo(self, videoNo):
        # print("post video")
        url = f"https://graph-video.facebook.com/{self.facebookId}/videos?access_token=" + self.facebookApi

        files = {
            'file': open(self.downloadedVideoPath[videoNo], 'rb'),
        }
        payload = {
            "title": self.downloadedVideoTitle[videoNo],
            "description": self.downloadedVideoTitle[videoNo],
        }
        st = requests.post(url, files=files, data=payload)
        # os.remove(self.downloadedVideoPath[videoNo])
        print(st.json())
        return st.json()['id']

    def uploadVideo(self):
        """upload new video to facebook"""
        for i in range(len(self.downloadedVideoPath)):
            self.postVideo(i)
        pass


facebookId = "DontBeCorner"


def uploadvideotest(videoPath):
    print("video upload")
    url = f"https://graph-video.facebook.com/{facebookId}/videos?access_token=" + access_token
    files = {
        'file': open(videoPath, 'rb'),
    }
    payload = {
        "title": "testing video",
        "description": 'summa oru video',
    }
    st = requests.post(url, files=files, data=payload)
    print(st.json())
    return st.json()['id']

# uploadvideotest("./Overcome your weakness ✌@Dont Be Corner.mp4")
# print("======================",exists("./Overcome your weakness ✌@Dont Be Corner.mp4"))
