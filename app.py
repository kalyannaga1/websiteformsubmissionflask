from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import urllib

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=formsubmissionserver1.database.windows.net;DATABASE=formsubmissionserver1;UID=kalyan;PWD=qwertynaga@1")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "UsersV1"

    fName = db.Column(db.String, primary_key=True)
    lName = db.Column(db.String)  # Added this line
    email = db.Column(db.String)

@app.route('/', methods=['GET', 'POST'])
def form_submit():
    if request.method == 'POST':
        fName = request.form.get('fname')
        lName = request.form.get('lname')  # Added this line
        email = request.form.get('email')

        user = User(fName=fName, lName=lName, email=email)  # Added lName in this line
        db.session.add(user)
        db.session.commit()

        return 'Form submitted successfully!'
    
    return render_template('submitform.html')

if __name__ == '__main__':
    app.run(port=8080)
