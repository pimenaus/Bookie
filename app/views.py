from app import app
from flask import flash, redirect, render_template, session, url_for,request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from app.forms import LoginForm
from app.models import User, ROLE_USER,ROLE_ADMIN
from werkzeug import generate_password_hash, check_password_hash
import json

@app.route('/')
@app.route('/index')
#@login_required
def index():
    user = g.user

    books = [
        {
            'author':{ 'first_name':'Frederich',
                       'last_name':'Brooks' },
            'title':'Mystical man-month'
        },
        {
            'author':{ 'first_name':'Edward',
                       'last_name':'Yordon' },
            'title':'Deathmarch'
        }]
    return render_template('index.html',
                           title = 'Home',
                           pill = 'home',
                           user = user,
                           books = books)


@app.route('/login', methods = ['GET','POST'])
#@oid.loginhandler
def login():
    return render_template('login.html', pill = 'login')
#    if g.user is not None and g.user.is_authenticated():
#        return redirect(url_for('index'))

#    form = LoginForm()
#    if form.validate_on_submit():
#        session['remember_me'] = form.remember_me.data
#        return oid.try_login(form.openid.data, ask_for=['nickname','email'])

#    return render_template('login.html',
#                           title = 'Sign In',
#                           form = form,
#                           providers = app.config['OPENID_PROVIDERS'])


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        user = User.query.filter_by(email = _username).first()
        if check_password_hash(user.hashed_password,_password):
            session['user'] = user.nickname
            return redirect('/index')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')

    except Exception as e:
        return render_template('error.html',error = str(e))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash("Invalid login. Please try again.")
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname,email=resp.email,role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me=False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me',None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/register')
def register():
    return render_template('register.html', pill = 'register')


@app.route('/onRegister', methods = ['POST'])
def onRegister():

    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = generate_password_hash(_password)

    if _name and _email and _password:
        user = User(nickname=_name,email=_email,hashed_password = _hashed_password,role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run()
