FROM python:3

ADD DiscordBot/ /
RUN python3 -m pip install --upgrade pip discord.py pyowm numpy requests gspread google-api-python-client

CMD [ "python3", "/BlenderBot.py" ]


