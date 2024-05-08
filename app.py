from flask import Flask,render_template,request,jsonify
from math import ceil

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pos'
db = SQLAlchemy(app)


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
@app.route('/catalog/category')
def category():
    return render_template('catalog/category.html')

@app.route('/delete/<string:id>', methods=['DELETE'])
def deleteRecord(id):
    category = Category.query.filter_by(id=id).first()
    if category:
        db.session.delete(category)
        db.session.commit()
        return "Record deleted successfully"
    else:
        return "Record not found or already deleted"
    

@app.route('/get-list')
def getList():

    rows = Category.query.all()
   
    data = [{'checkbox': f''' 
                    <div class="flex items-center">
                        <input value="{row.id}" type="checkbox"
                            class="checkbox w-4 h-4 text-green-600 bg-gray-100 border-gray-300 rounded focus:ring-green-500 dark:focus:ring-green-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                    </div>
                ''',
             'id': row.id,
             'name': row.name,
             'status': '<div class="bg-green-600 text-white py-1 rounded-sm text-center text-xs">Active<div>' if row.status==1 else '<div class="bg-red-500 text-white py-1 rounded-sm text-center text-xs">Not Active</div>' ,
             'created_at': row.created_at.strftime('%d-%m-%Y %H:%M'),
             'updated_at': row.updated_at.strftime('%d-%m-%Y %H:%M'),
             'action':f'''
             <button type="button" onclick="editRecord('{row.id}')" class="text-base bg-gray-200 rounded-md text-xs w-7 h-7 me-1 dark:bg-gray-700 "><i class="fa-light fa-pen"></i></button>
             <button type="button" onclick="deleteRecord('{row.id}')" class="text-base bg-gray-200 rounded-md text-xs w-7 h-7 me-1 dark:bg-gray-700 "><i class="fa-light fa-trash"></i></button>
             ''',
             } 
            for row in rows]
        
    response = {'data': data}

    return jsonify(response)

# start 
if __name__ == '__main__':
    app.run(debug=True)

