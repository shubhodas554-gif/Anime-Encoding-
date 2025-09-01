AutoAnimeBot - The Ultimate Anime Uploader Bot
This is an automated Telegram bot designed to download and upload anime episodes to a designated Telegram channel.
Features
 * Automated Downloads: Downloads episodes from specified sources.
 * Smart Thumbnails: Generates custom thumbnails for each video with episode info, file size, and duration.
 * Progress Tracking: Provides real-time progress updates for downloads and uploads.
 * Inline Buttons: Adds inline buttons for viewers to vote on episodes and navigate to discussions.
 * Schedule Updates: Keeps a channel updated with a daily anime schedule.
Setup and Installation
1. Clone the repository
git clone [https://github.com/your-username/AutoAnimeBot.git](https://github.com/your-username/AutoAnimeBot.git)
cd AutoAnimeBot

2. Install dependencies
It is highly recommended to use a virtual environment.
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

3. Configure the bot
Create a config.py file in the main directory and fill it with your credentials and channel IDs. Use the config_template.py as a reference.
4. Run the bot
python -m AutoAnimeBot

Configuration
Edit the config.py file to set your API credentials and channel details.
 * API_ID: Your Telegram API ID.
 * API_HASH: Your Telegram API Hash.
 * BOT_TOKEN: Your bot's token from BotFather.
 * UPLOADS_CHANNEL_ID: The ID of the channel where videos will be uploaded.
 * INDEX_CHANNEL_USERNAME: The username of your index channel.
 * COMMENTS_GROUP_LINK: The invite link for your discussion group.
 * SCHEDULE_MSG_ID: The message ID of the bot's schedule message.
 * STATUS_MSG_ID: The message ID of the bot's status message.
 * SLEEP_TIME: Time to sleep between uploads.
