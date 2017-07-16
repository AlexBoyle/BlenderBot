from Utility.sqlUtility import *

class TermService:
  def __init__(self, server_id):
    try:
      self.sql = sql()
      self.server = server_id
      self.isSetup = True
    except Exception as inst:
      print(inst)
      self.isSetup = False

  def getTerm(self, num):
    return self.sql.query("SELECT * FROM terms WHERE server_id=" + str(self.server) + " AND num=" + str(num))[0]

  def getLen(self):
    if(self.isSetup):
      return self.sql.query("SELECT COUNT(num) AS length FROM terms WHERE " + str(self.server))[0]['length']
    else:
      return 0

  def getSearch(self, search):
    if(self.isSetup):
      return self.sql.query("SELECT num, content FROM terms WHERE server_id=" + self.server + " AND content LIKE " + '"%' + search + '%"')
    else:
      return "Somthing Went Wrong"
  def newTerm(self, term):
    ''
  def editTerm(self, num, term):
    ''
  def rmTerm(self, num):
    ''