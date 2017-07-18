from Global import *
import pymysql
import pymysql.cursors
from pymysql.charset import *
from pymysql.charset import _charsets
_charsets.add(Charset(255, 'utf8', 'utf8_unicode_ci', ''))
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
  def query(self, query, params = None):
    cursor = self.db.cursor()
    cursor.execute(query, params)
    out = cursor.fetchall()
    self.db.commit()
    cursor.close()
    return out

