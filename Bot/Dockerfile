FROM python:3

RUN python3 -m pip install --upgrade pip discord.py pyowm numpy requests gspread google-api-python-client PyMySQL
ADD BlenderBot/ /
CMD [ "python3", "/BlenderBot.py" ]
