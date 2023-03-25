from flask import Flask, render_template, jsonify
from database import load_jobs, load_job

app = Flask(__name__)


@app.route("/")
def hello_jovain():
  jobs = load_jobs()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_id(id):
  job = load_job(id)

  if not job:
    return "Not Found", 404
  else:
    return render_template('joblist.html', jobs=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
