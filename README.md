# manga-discord-bot

## What is manga-discord-bot?
manga-discord-bot (temporary name) is a discord bot to read manga from [readm.org](https://readm.org/)

## Installation

### Locally

Clone the repo:

```bash
git clone https://github.com/ayylouu/manga-discord-bot.git
cd manga-discord-bot
```

Install requirements:

```bash
pip install beautifulsoup4
```

Create a discord bot ([guide](https://discord.com/developers/docs/intro#bots-and-apps)) and copy the token.
then paste your token in [config.json](https://github.com/ayylouu/manga-discord-bot/blob/master/config.json):

```json
{
	"token": "your token"
}
```

Start the bot:

```bash
python ./main.py
```

## Usage
For now there is only one command (more comming soon)
+ read manga_number chapter_number
![screenshot](https://github.com/ayylouu/manga-discord-bot/blob/master/screenshots/read.png)

## TODO
- [ ] Heroku installation
- [X] Local hosting
- [ ] Dockerfile
- [ ] Search manga by name
- [ ] List all manga chapters
- [ ] Read manga by name
- [ ] Get notified when new chapter is available
