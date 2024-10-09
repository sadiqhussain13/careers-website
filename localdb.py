import os
import psycopg2
import dotenv

dotenv.load_dotenv()

# Load jobs from database
def load_jobs_from_db():
  try:
    conn = psycopg2.connect(
      host=os.environ.get('DATABASE_HOST'),
      database=os.environ.get('DATABASE_NAME'),
      user=os.environ.get('DATABASE_USERNAME'),
      password=os.environ.get('DATABASE_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM jobs")
    results = cur.fetchall()
    jobs = []
    for row in results:
      job = {
        'id': row[0],
        'title': row[1],
        'location': row[2],
        'salary': row[3],
        'currency': row[4],
        'responsibilities': row[5],
        'requirements': row[6]
      }
      jobs.append(job)
    conn.close()
    return jobs
  except psycopg2.Error as e:
    print(f"Error loading jobs from database: {e}")

def load_job_from_db(id):
  try:
    conn = psycopg2.connect(
      host=os.environ.get('DATABASE_HOST'),
      database=os.environ.get('DATABASE_NAME'),
      user=os.environ.get('DATABASE_USERNAME'),
      password=os.environ.get('DATABASE_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM jobs WHERE id = %s", (id,))
    results = cur.fetchall()
    if not results:
      return None
    job = {
      'id': results[0][0],
      'title': results[0][1],
      'location': results[0][2],
      'salary': results[0][3],
      'currency': results[0][4],
      'responsibilities': results[0][5],
      'requirements': results[0][6]
    }
    conn.close()
    return job
  except psycopg2.Error as e:
    print(f"Error loading job from database: {e}")

# # To check the type
# print("type of results: ", type(load_jobs_from_db()))
# print(load_jobs_from_db())