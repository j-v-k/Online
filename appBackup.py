# We need to import request to access the details of the POST request 
# and render_template, to render our templates (form and response)if 
# __name__ == '__main__': we'll use url_for to get some URLs for the app 
# on the templates app.run(debug=True)
from flask import Flask, render_template, request, url_for
# Initialize the Flask application
app = Flask(__name__)
# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')
# Define a route for the action of the form, for example '/hello/' We 
# are also defining which type of requests this route is accepting: POST 
# requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    from flask import Flask
    from flaskext.mysql import MySQL
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'pies'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    query = request.form['yourname']
    mysql.init_app(app)
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
	cursor.execute(query)
    except:
	print "SQL is wrong"
	db.session.rollback()
    name0 =str(cursor.fetchone()).replace("(", "")
    name1 =str(cursor.fetchone()).replace(")", "")
    name = name1
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)
# Run the app :)


if __name__ == '__main__':
    app.run(debug=True)
