import os
from sqlalchemy import create_engine, text
#Connecting database
db_connect = os.environ['DB_CONNECTION']

engine = create_engine(db_connect,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    result_all = result.fetchall()

    jobs = []
    for row in result_all:
      jobs.append(dict(zip(result.keys(), row)))
  return jobs


def load_job(id):
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs where id = :val "),
                                {'val': id})
    row = result.fetchone()
    if row is None:
      return None
    else:
      return dict(zip(result.keys(), row))
