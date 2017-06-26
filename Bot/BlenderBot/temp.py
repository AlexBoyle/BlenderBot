import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Utility:
  sheet = {}
  server_ids = []
  def __init__(self):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Files/client_secret.json', scope)
    client = gspread.authorize(creds)
    self.sheet = client.open("ServerSettings").sheet1
    self.sheet = self.sheet.get_all_values()
    for row in self.sheet:
      if(row[0].isnumeric()):
        self.server_ids.append(row[0])
  def get_server_ids(self):
    return self.server_ids
