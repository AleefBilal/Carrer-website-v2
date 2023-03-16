from sqlalchemy import create_engine, text
#Connecting database
db_connect = "mysql+pymysql://qyhj9utvpud0fyt7bcur:pscale_pw_OrKB05nSNmWRKlojyfvYysULci4BhUxR5vM0CS5mx9z@ap-south.connect.psdb.cloud/db_demo?charset=utf8mb4"

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
