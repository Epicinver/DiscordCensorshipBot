# Discord Censorship Bot
A Discord bot that censors messages.


# How do I use the bot?
Open a terminal in the directory that the script is in. 
Type pip install -r requirements.txt OR if you are on Linux/macOS, type pip3 install -r requirements.txt.
Open the .env file and paste your bot's token after **"DISCORD_TOKEN"**.
Run main.py on a secure server OR run it locally.
Invite your bot into your server and say a word that is censored.
It should delete your message and say "dont do that :( @YourDiscordName".
-

How do I invite the bot into the server?
Go to the [Discord Developer Portal](https://discord.com/developers/applications/) and copy the application ID of the bots application.
Paste the ApplicationID into this URL after "client_id=". https://discord.com/oauth2/authorize?client_id=[ApplicationID]&scope=bot
Add it to a server, as you would do with any other bot.
