# "Database code" for the DB Forum.

import datetime
'''
POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))
'''

import psycopg2, bleach
import os

#DBNAME = "forum"
DATABASE_URL = os.environ['DATABASE_URL']


def get_posts():
  """Return all posts from the 'database', most recent first."""
  #db = psycopg2.connect(database=DBNAME,user='postgres')
  db = psycopg2.connect(DATABASE_URL, sslmode='require')
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  #db = psycopg2.connect(database=DBNAME,user='postgres')
  db = psycopg2.connect(DATABASE_URL, sslmode='require')
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()

