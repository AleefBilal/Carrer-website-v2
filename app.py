from flask import Flask, render_template, jsonify, request
from database import load_jobs, load_job, add_app_db

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


@app.route("/jobs/<id>/apply", methods=['post'])
def apply_job(id):
  data = request.form
  job = load_job(id)
  add_app_db(id, data)
  return render_template('app_submit.html', application=data, job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
