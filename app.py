from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pos'
db = SQLAlchemy(app)

# Function to fetch data for the current page
def get_data_for_page(page_num, per_page):
    offset = (page_num - 1) * per_page
    return Category.query.limit(per_page).offset(offset).all()


class Category(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# /////////////////// routes ///////////////////
# /common
@app.route('/')
def home():
    return render_template('common/home.html')

@app.route('/login')
def login():
    return render_template('common/login.html')

@app.route('/pos')
def pos():
    return render_template('common/pos.html')

# /catalog
@app.route('/catalog/categories')
def categories():
    page = int(request.args.get('page', 1))
    per_page = 8
    data = get_data_for_page(page, per_page)

    total_items = Category.query.count()

    total_pages = (total_items + per_page - 1) // per_page
    
    return render_template('catalog/categories.html',list=data,page=page, total_pages=total_pages,total_items=total_items)


# start 
if __name__ == '__main__':
    app.run(debug=True)
