<h1 align="center"><b>Leo Media Search Bot 🇱🇰</b></h1>

# Features 

* Index channel or group files for inline search.
* When you post file on telegram channel or group this bot will save that file in database, so you can search easily in inline mode.
* Supports document, video and audio file formats with caption support.
* Broadcast to the all of users in database
* Can view user stats in bot's database
* Can ban or unban any user from database

<p align="center">
  <img src="https://telegra.ph/file/c705fac44db2b8d7f47e7.jpg"></p>

<p align="center">
    <a href="https://github.com/Naviya2/LeoMediaSearchBot"> <img src="https://img.shields.io/github/repo-size/Naviya2/LeoMediaSearchBot?color=orange&logo=github&logoColor=green&style=for-the-badge" /></a>
    <a href="https://github.com/Naviya2/LeoMediaSearchBot/commits/Naviya2"> <img src="https://img.shields.io/github/last-commit/Naviya2/LeoMediaSearchBot?color=brown&logo=github&logoColor=green&style=for-the-badge" /></a>
    <a href="https://github.com/Naviya2/LeoMediaSearchBot/issues"> <img src="https://img.shields.io/github/issues/Naviya2/LeoMediaSearchBot?color=blueviolet&logo=github&logoColor=green&style=for-the-badge" /></a>
    <a href="https://github.com/Naviya2/LeoMediaSearchBot/network/members"> <img src="https://img.shields.io/github/forks/Naviya2/LeoMediaSearchBot?color=red&logo=github&logoColor=green&style=for-the-badge" /></a></p>

## Installation

### Easy Way
## Deploy To Heroku

<details>
  <summary><b>Deploy on Heroku</b></summary>
<br>

<p align="left">
  <a href="https://heroku.com/deploy?template=https://github.com/Naviya2/LeoMediaSearchBot/tree/leo">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a>
</p>
  
</details>
  

### Hard Way

```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
env\Scripts\activate.bat # For Windows
source env/bin/activate # For Linux or MacOS

# Install Packages
pip3 install -r requirements.txt

# Edit info.py with variables as given below then run bot
python3 bot.py
```
Check [`sample_info.py`](sample_info.py) before editing [`info.py`](info.py) file

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB]
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com)
* `BOT_OWNER` : user id of the owner
* `SESSION` : A session name for save users in db.
* `BOT_USERNAME` : Bot' username . Get it from botfather..
* `UPDATES_CHANNEL`: Username or ID of channel. Without subscribing this channel users cannot use bot.

### Optional Variables
* `COLLECTION_NAME`: Name of the collections. Defaults to Telegram_files. If you going to use same database, then use different collection name for each bot
* `MAX_RESULTS`: Maximum limit for inline search results
* `CACHE_TIME`: The maximum amount of time in seconds that the result of the inline query may be cached on the server
* `USE_CAPTION_FILTER`: Whether bot should use captions to improve search results. (True/False)
* `AUTH_USERS`: Username or ID of users to give access of inline search. Separate multiple users by space. Leave it empty if you don't want to restrict bot usage.
* `LOG_CHANNEL`: a channel id for save all the logs of bot
* `START_MSG`: Bot's Start Msg.
* `USERBOT_STRING_SESSION`: User bot string session.

## Admin commands
```
channel - Get basic infomation about channels
total - Show total of saved files
delete - Delete file from database
index - Index all files from channel or group
logger - Get log file
stats - get recent user stats
broadcast - broascast any message to all the users of bot
banuser - to ban a user from database
unbanuser - to unban a user from database
bannedusers - Get banned users list
```

## Tips
* Use `index` command or run [one_time_indexer.py](one_time_indexer.py) file to save old files in the database that are not indexed yet.
* You can use `|` to separate query and file type while searching for specific type of file. For example: `Avengers | video`
* If you don't want to create a channel or group, use your chat ID / username as the channel ID. When you send a file to a bot, it will be saved in the database.

---

## Contributions
Contributions are welcome.

## Special Thanks 
Imported some codes from [Media Search Repo](https://github.com/Mahesh0253/Media-Search-bot) ❤️

### Support Group 🇱🇰
<a href="https://t.me/leosupportx"><img src="https://img.shields.io/badge/Telegram-Join%20Support%20Group-blue.svg?logo=telegram"></a>
 
### Updates Channel 🇱🇰
<a href="https://t.me/new_ehi"><img src="https://img.shields.io/badge/Telegram-Join%20Updates%20Channel-blue.svg?logo=telegram"></a>

