from mysql import connector

class UseDatabase:
   """this class is a context manager desinged to work with python with statement.
   implementation of this class automatically consider setup and teardown process involved in with statement
   """
   def __init__(self, config:dict):
      super().__init__()
      self.configuration = config
   
   def __enter__(self):
      self.conn = connector.connect(**self.configuration)
      self.cursor = self.conn.cursor()
      return self.cursor

   def __exit__(self, exc_type, exc_value, exc_trace):
      self.conn.commit()
      self.cursor.close()
      self.conn.close()
