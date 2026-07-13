from app.extensions import db

class Posts(db.Model):
    __tablename__ = 'postsdb'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    snippet = db.Column(db.Text)
    full_content = db.Column(db.Text)
    img_url = db.Column(db.Text)
    category_data = db.Column(db.Text) 
    created_date = db.Column(db.Text)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class User(db.Model):
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)