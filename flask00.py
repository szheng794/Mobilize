# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)     # create an app

posts = { 1: {'subject': 'First post', 'text': 'This is my first post', 'date': '10-1-2020'},
          2: {'subject': 'Second post', 'text': 'This is my second post', 'date': '10-2-2020'},
          3: {'subject': 'Third post', 'text': 'This is my third post', 'date': '10-3-2020'}
        }

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/')
@app.route('/index')
def index():
   a_user = {'name': 'Prachi', 'email': 'mogli@uncc.edu'}
   return render_template('index.html', user = a_user)

@app.route('/feed')
def get_posts():
   a_user = {'name': 'Prachi', 'email': 'pyadav5@uncc.edu'}

   return render_template('feed.html', posts=posts)

@app.route('/singlePost/<post_id>')
def get_post(post_id):
   a_user = {'name': 'Prachi', 'email': 'pyadav5@uncc.edu'}

   return render_template('singlePost.html', post=posts[int(post_id)])


@app.route('/feed/newPost',methods=['GET','POST'])
def new_post():
   # create mock user
   a_user = {'name': 'Prachi', 'email': 'pyadav5@uncc.edu'}

   # check method used for request
   print('request method is',request.method)
   if request.method == 'POST':
       # get title data
       subject = request.form["subject"]
       # get note data
       text = request.form['noteText']
       # create date stamp
       from datetime import date
       today = date.today()
       # format date mm/dd/yyyy
       today = today.strftime("%m-%d-%Y")
       # get the last ID used and increment by 1
       id = len(posts)+1
       # create new note entry
       posts[id] = {'subject': subject, 'text': text, 'date': today}
       # ready to render response - recirect to notes listing
       return redirect(url_for('get_posts'))
   else:
       # GET request -show new note form
       return render_template('newPost.html', user=a_user)




app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# post that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
