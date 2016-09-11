# We need to import request to access the details of the POST request 
# and render_template, to render our templates (form and response)if 
# __name__ == '__main__': we'll use url_for to get some URLs for the app 
# on the templates app.run(debug=True)
from flask import Flask, render_template, request, url_for
from flaskext.mysql import MySQL

MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = ''
MYSQL_DATABASE_DB = 'pies'
MYSQL_DATABASE_HOST = 'localhost'




# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(__name__)
mysql = MySQL(app)
# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')
# Define a route for the action of the form, for example '/hello/' We 
# are also defining which type of requests this route is accepting: POST 
# requests in this case
@app.route('/hello/', methods=['POST'])

def hello():
    conn = mysql.get_db()
    try:
	print name
    except:
	print "no name"
    query = request.form['yourname']
    with conn as cursor:
	 try:
 	 	cursor.execute(query)
                name = str(cursor.fetchone())
         except:
		name = "SQL is wrong"
    return render_template('form_action.html', name=name)
# Run the app :)


if __name__ == '__main__':
    app.run(debug=True)
    sys.exit (1)
