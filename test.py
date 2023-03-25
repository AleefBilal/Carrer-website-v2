from sqlalchemy import create_engine, text
import os

db_connect = os.environ['DB_CONNECTION']

engine = create_engine(db_connect,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_job():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs where id = :val "),
                                val=id)
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      return rows[0]
