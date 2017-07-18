from Utility.sqlUtility import *

class TermService:
  def __init__(self, server_id):
    self.isSetup = True
    if ((type(server_id) is str and server_id.isdigit()) or type(server_id) is int):
      self.server = str(server_id)
    else:
      self.isSetup = False
    try:
      self.sql = sql()
    except Exception as inst:
      self.isSetup = False

  def getTerm(self, num):
    if(self.isSetup and ((type(num) is str and num.isdigit()) or type(num) is int)):
      return self.sql.query("SELECT * FROM terms WHERE server_id = %s AND num = %s", [self.server, num])[0]
    else:
      return "Somthing Went Wrong"

  def getLen(self):
    if(self.isSetup):
      return self.sql.query("SELECT MAX(num) AS length FROM terms WHERE server_id = %s", [self.server])[0]['length']
    else:
      return "Somthing Went Wrong"

  def getSearch(self, search):
    if(self.isSetup):
      return self.sql.query("SELECT num, content FROM terms WHERE server_id= %s AND content LIKE %s", [self.server, search])
    else:
      return "Somthing Went Wrong"
  def newTerm(self, term):
    if(self.isSetup):
      return self.sql.query("INSERT INTO terms (server_id, num, content) SELECT %s, MAX(num) + 1, %s FROM terms;", [self.server, term])
    else:
      return "Somthing Went Wrong"
  def editTerm(self, num, term):
    if(self.isSetup):
      return self.sql.query("UPDATE terms SET content = %s WHERE server_id = %s AND num = %s", [term, self.server, term])
    else:
      return "Somthing Went Wrong"
  def rmTerm(self, num):
    if(self.isSetup):
      return self.sql.query("DELETE FROM terms WHERE server_id = %s AND num = %s;UPDATE terms SET num = num - 1 WHERE num > %s" , [self.server, num, num])
    else:
      return "Somthing Went Wrong"
  def checkSetup(self):
    query = (
      "CREATE TABLE IF NOT EXISTS `servers` ("
      "  `id` int(11) NOT NULL UNIQUE,"
      "  `name` char(64) NOT NULL,"
      "  PRIMARY KEY  (`id`)"
      ");"
      "CREATE TABLE IF NOT EXISTS `terms` ("
      "  `server_id` int(11) NOT NULL,"
      "  `id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,"
      "  `num` int(11) NOT NULL,"
      "  `content` CHAR(256) NOT NULL,"
      "  FOREIGN KEY (id) REFERENCES servers(id),"
      "  PRIMARY KEY  (`id`)"
      ");"
    )
    return self.sql.query(query)
