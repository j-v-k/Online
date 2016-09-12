 

# We need to import request to access the details of the POST request 
# and render_template, to render our templates (form and response)if 
# __name__ == '__main__': we'll use url_for to get some URLs for the app 
# on the templates app.run(debug=True)
from flask import Flask, render_template, request, url_for
from flaskext.mysql import MySQL

MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = ''
MYSQL_DATABASE_DB = 'NBA'
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



@app.route('/foo/', methods=['POST'])
def foo():
    return render_template('data_map_and_ex_qs.html')



@app.route('/results/', methods=['POST'])

def results():
    conn = mysql.get_db()
    try:
          print name
    except:
          print "no name"
    query = request.form['yourname']
    x = request.form['formatlist']
#    print x
    with conn as cursor:
         cursor.execute(query)
         row = cursor.fetchall()
         rowList = [[i[0] for i in cursor.description]]
      
         for i in row:
                rowList += [list(i)]
 #        print rowList       
         if "CSV" or "Table" in x:
               name = []
               for row in rowList:
	           # print row
                   # print 77777777
                    queryList  = []
                    if "CSV" in x:
                   	 for i in row:
                         	# print i
                         	 queryList += [str(i).encode('utf-8')]
                   	 name += [str(queryList).replace("]","").replace("[","")]
                    else: 
                        for i in row:
                                # print i
                                 queryList += [str(i).encode('utf-8')]
                        name += [queryList]
               name = (name, query)
               if "CSV" in x:
                     return render_template('form_action.html', name=name)
               else:
                     return render_template('form_action_table.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
    sys.exit (1)
