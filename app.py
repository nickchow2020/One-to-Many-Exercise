"""Blogly application."""

from flask import Flask,request,render_template,redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,User,Post

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'is so secret keys'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def home_page():
    return redirect("/users")

@app.route("/users")
def all_users():
    all_user = User.query.all()
    return render_template("all_user.html",users=all_user)

@app.route('/users/new')
def add_user_form():
    return render_template("add_user.html")

@app.route('/users/new',methods=["POST"])
def post_user_form():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["user_url"]

    new_user = User(first_name=first_name,last_name=last_name,image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    target_user = User.query.get(user_id)
    user_post = Post.query.filter(Post.user_id == user_id)
    return render_template("user_detail.html",user=target_user,post=user_post)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    target_user = User.query.get(user_id)
    return render_template("edit_user.html",user=target_user)

@app.route('/users/<int:user_id>/edit',methods=["POST"])
def save_edit(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['user_url']

    target_user = User.query.get(user_id)

    target_user.first_name = first_name
    target_user.last_name = last_name
    target_user.image_url = image_url

    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete',methods=["POST"])
def delete_user(user_id):
    get_user_info = User.query.get(user_id)
    delete_user = User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return render_template('delete_user.html',user=get_user_info)

@app.route('/users/<int:user_id>/post/new')
def show_post_form(user_id):
    user = User.query.get(user_id)
    return render_template('post_form.html',user=user)


@app.route('/users/<int:user_id>/post/new',methods=["POST"])
def post_form(user_id):
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title,content=content,user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>')
def add_post(post_id):
    post = Post.query.get(post_id)
    return render_template("post_detail.html",post=post)

@app.route('/posts/<int:post_id>/edit')
def show_post_edit(post_id):
    post = Post.query.get(post_id)
    return render_template('post_edit.html',post=post)

@app.route("/posts/<int:post_id>/edit",methods=["POST"])
def post_edit(post_id):
    post = Post.query.get(post_id)

    title = request.form["title"]
    content = request.form["content"]

    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()

    return redirect(f"/posts/{post_id}")

@app.route("/posts/<int:post_id>/delete",methods=["POST"])
def post_delete(post_id):
    user = Post.query.filter_by(id=post_id)

    target_user = user.first()

    user_id = target_user.user.id
    
    user.delete()
    db.session.commit()
    return redirect(f"/users/{user_id}")