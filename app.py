from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'Location': 'Lahore',
  'Salary': '150,000'
}, {
  'id': 2,
  'title': 'Penetration Testing',
  'Location': 'Islamabad',
  'Salary': '120,000'
}, {
  'id': 3,
  'title': 'UI/UX Engineer',
  'Location': 'Jhelum',
  'Salary': '150,000'
}, {
  'id': 4,
  'title': 'Project Manager',
  'Location': 'Lahore',
}]


@app.route("/")
def hello_jovain():
  return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
