from flask import Flask, render_template
import util


app = Flask(__name__)
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'
# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route("/api/update_basket_a")

def index():
    # this is your index page
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_commit_sql(cursor, connection, sql_string="INSERT INTO basket_a VALUES(5, 'Cherry');")
    if record == -1:
        # you can replace this part with a 404 page
        log = 'Error'
        print('Error')
    else:
        
        log = 'Success'
        print('Success')
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
    
