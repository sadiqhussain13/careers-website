from flask import Flask, render_template, jsonify
from localdb import load_jobs_from_db, load_job_from_db

app = Flask(__name__)
@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

# API for list of jobs  
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify([jobs])

@app.route("/job/<id>")
def get_job(id):
  job = load_job_from_db(id)
  if not job:
    return 'Not found', 404
  return render_template('jobpage.html', job=job)

print(__name__)
if (__name__) == "__main__":
  app.run(host='0.0.0.0',debug=True, port=8080)