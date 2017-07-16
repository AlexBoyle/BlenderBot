from Global import *
import pymysql
import pymysql.cursors
#Hack to get sql to work
from pymysql.charset import *
from pymysql.charset import _charsets
_charsets.add(Charset(255, 'utf8', 'utf8_unicode_ci', ''))
#End of hack
class sql:
  db = None
  def __init__(self):
    self.db = pymysql.connect(
      host = db_host,
      port = db_port,
      user = db_user,
      passwd = db_pass,
      db = db_databace,
      charset = 'utf8',
      cursorclass=pymysql.cursors.DictCursor
    )

  def prepareDatabase(self):
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
  def query(self, query):
    cursor = self.db.cursor()
    cursor.execute(query)
    out = cursor.fetchall()
    cursor.close()
    return out
