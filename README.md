![Face](http://i.imgur.com/5fBK3NV.jpg)
# BlenderBot
## Notes
  This Bot was written by Alex Boyle and Rishabh Ekbote  
With special assistance from Gary, Tyler, Otto, Pat and Nick <3

  This bot is open source(github linked below) and if you happen to use and files or major code blocks from this project accredidation is appreciated.  
## Setup
- Install the latest version of docker
- Fill in the `Global.py.default` file and rename to `Global.py` 
- Fill in the `client_secret.json.default` file and rename to `client_secret.json`  
## Running  
### Docker  
- install Docker   
`sudo apt-get install docker.io`  
- Run BlenderBot  
`docker-manager -b -i blender-bot start`  
### Unix
- Install dependencies  
`python3 -m pip install --upgrade pip discord.py pyowm numpy requests gspread google-api-python-client`  
- Run  
`./DiscorcBot/BlenderBot.py`  
