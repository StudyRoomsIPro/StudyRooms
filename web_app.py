from flask import (
    Flask,
    g,
    render_template,
    url_for, 
    flash, 
    redirect, 
    request, 
    session, 
    abort
)
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password   
    def __repr(self):
        return f'<User: {self.username}>'
users = []
users.append(User(id=1, username='max@hawk.iit.edu', password='123'))
users.append(User(id=2, username='bob@hawk.iit.edu', password='321'))
app = Flask(__name__)
app.secret_key = 'asd'

@app.before_request
def before_request():
    if 'user_id' in session:
        user =[x for x in users if x.id == session['user_id']][0]
        g.user = user
    else:
        g.user = None

@app.route('/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/scheduling')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('scheduling.html')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.static_folder='static'
    app.run(debug=True)

