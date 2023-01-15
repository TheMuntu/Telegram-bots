import telegram
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json

# Initialize the Telegram bot
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Handle the '/download' command
def download(update, context):
    # Get the video link from the user
    video_link = update.message.text.split()[1]
    # Get the video id from the link
    video_id = video_link.split("/")[-1]
    # Get the video url using the video id and linkedin api
    url = f"https://www.linkedin.com/voyager/api/feed/richVideoView?key={video_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "TE": "Trailers",
        "X-LinkedIn-Id": "",
        "X-RestLi-Protocol-Version": "2.0.0",
        "Csrf-Token": "ajax:3824906570822090722",
        "Csrf-Token": "ajax:3824906570822090722",
        "X-LI-Lang": "en_US",
        "X-LI-Track": "{\"clientVersion\":\"1.74.0\",\"osName\":\"Windows\",\"osVersion\":\"10\",\"browserName\":\"Chrome\",\"browserVersion\":\"89\"}",
        "X-LI-Page-Instance": "urn:li:page:d_flagship3_feed;CXjq3JlxQVm/FsdYmDV7jA==",
        "X-LI-UUID": "CXjq3JlxQVm/FsdYmDV7jA==",
        "X-LI-Route-Key": "",
        "X-LI-Orig-Url": "https://www.linkedin.com/feed/update/urn:li:richVideo:6778465513555927040",
    }
    # getting the json data
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    video_url = data["value"]["playable"]["url"]
    # Download the video
    video = requests.get(video_url)
    open("video.mp4", "wb").write(video.content)
    # Send the video to the user
    context.bot.send_video(chat_id=update.message.chat_id, video=open('video.mp4', 'rb'))
