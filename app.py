from flask import Flask,render_template,request,redirect

app = Flask(__name__)
admins = [{
    "username" : "aswnss",
    "password" : "password"
},{
    "username" : "sctcl",
    "password" : "root"
}]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        givenusrnm = request.form['Username']
        givenpswd = request.form['Password']
        for admin in admins:
            if admin['username'] ==givenusrnm and admin['password'] == givenpswd:
                return redirect('/admin/' + admin['username'])
            else:
                return redirect('#')
    return render_template('admin-verify.html')

if __name__ == '__main__':
    app.run(debug=True)
    