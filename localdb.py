import os
import psycopg2
import dotenv

dotenv.load_dotenv()

# Load jobs from database
def load_jobs_from_db():
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

# # To check the type
# print("type of results: ", type(load_jobs_from_db()))
# print(load_jobs_from_db())