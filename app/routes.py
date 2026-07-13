from flask import render_template,request,redirect,url_for,flash
from app.models import Posts,Category,User
from app.main import app,db

@app.route("/home")
def home():
   category  =  Category.query.all()
   post= Posts.query.all()
   return render_template("home.html",category=category,post=post)


@app.route("/posts/<category>/<title>")
def posts(category,title):
    category  =  Category.query.all()
    title=title.replace("-"," ")
    post= Posts.query.filter_by(title=title).all()
    if post:
      return render_template("posts.html",category=category,post=post)
    else:
       return "No data found"


@app.route("/")
@app.route("/login",methods=["POST","GET"])
def login():
    error="false"
    if request.method=="POST":
        data=request.form
        username=data.get("username")
        password=data.get("password")              
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            print("Login success")   
            return redirect(url_for('home'))
        else:
            error="true"
            return redirect(url_for('login', error=error))   
    signup = request.args.get("signup")    
    error = request.args.get("error") 
    return render_template("login.html", error=error,signup=signup)   
          

@app.route("/signup",methods=["POST","GET"])
def signup():  
   signup="false" 
   if request.method == "POST":
     user=User(username=request.form.get("username"),email=request.form.get("email"),password=request.form.get("password"))
     db.session.add(user)
     db.session.commit()
     signup="true"
     return redirect(url_for("login",signup=signup))
   return render_template("login.html")    


@app.route("/addBlog",methods=["POST","GET"])
def addBlog():
    addBlog="false"
    if request.method=="POST":  
      post=Posts(title= request.form.get("title"),snippet=request.form.get("snippet"),full_content=request.form.get("full_content"),img_url=request.form.get("img_url"),category_data=request.form.get("category_data"),created_date=request.form.get("created_date"))
      db.session.add(post)
      db.session.commit()
      addBlog="true"
      return redirect(url_for("addBlog",success=addBlog))
    return render_template("addBlog.html")