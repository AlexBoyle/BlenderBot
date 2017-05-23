FROM python:3

ADD DiscordBot/ /
RUN python3 -m pip install discord.py
RUN python3 -m pip install pyowm
RUN python3 -m pip install numpy
RUN python3 -m pip install requests
RUN python3 -m pip install --upgrade google-api-python-client
RUN python3 -m pip install gspread
CMD [ "python3", "/BlenderBot.py" ]


