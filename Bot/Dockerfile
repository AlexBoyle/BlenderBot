FROM python:3

RUN python3 -m pip install --upgrade pip discord.py pyowm numpy requests gspread mysql-connector-python-rf google-api-python-client
ADD BlenderBot/ /
CMD [ "python3", "/BlenderBot.py" ]
