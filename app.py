from flask import Flask,render_template, request, Response, jsonify
import mysql.connector 
import json

##set this value to your Mysql Daatabasee host IP aadddress
whichhost = ''
mysqluser = 'webdev'
mysqlpass = 'webdev'

app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('hello.html',webpagetitle="WebDevClass")



@app.route('/chatdata', methods=['GET'])
def chatdata():
    try:
        cnx = mysql.connector.connect(user=mysqluser,password=mysqlpass,host=whichhost,database='webdev')
        cursor = cnx.cursor(dictionary=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    query = ("SELECT id,comment,DATE_FORMAT(commenttime,'%M, %D %Y %H:%i') as 'commentdate' from chatdb order by commenttime")
    cursor.execute(query)
    data1 = cursor.fetchall()
    print(data1)
    return Response((json.dumps(data1)),mimetype='application/json')

@app.route('/newtext', methods=['POST'])
def newtext():
    if request.form.get('newcomment') is None or request.form.get('newcomment') == '':
            print("no post")
            print(request.form.get('newcomment'))
            return Response('{"Status":"No Data to Post"}',mimetype='application/json')
    try:
        cnx = mysql.connector.connect(user=mysqluser,password=mysqlpass,host=whichhost,database='webdev')
        cursor = cnx.cursor()
        print("INSERT into `chatdb` (`comment`) VALUES ('"+request.form.get('newcomment')+"')")
        query = ("INSERT into `chatdb` (`comment`) VALUES ('"+request.form.get('newcomment')+"')")
        cursor.execute(query)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
           return Response('{"Status":"Failure1"}',mimetype='application/json')
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            return Response('{"Status":"Faiilure2"}',mimetype='application/json')
        else:
           return Response('{"Status":"Failure3'+str(err)+'"}',mimetype='application/json')
 
    return Response('{"Status":"Success"}',mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)