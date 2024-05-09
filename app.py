from flask import Flask,render_template,request,jsonify
from urllib.parse import parse_qs


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pos'
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
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

@app.route('/delete/<int:id>', methods=['DELETE'])
def deleteRecord(id):
    category = Category.query.filter_by(id=id).first()
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'msg':'Category delete Successfully'}),200
    else:
        return jsonify({'msg':'Category has either been deleted or does not exist'}),500
    

@app.route('/insert', methods=['POST'])
def insertRecord():
    data = request.form.get('data')
    parseData = parse_qs(data)
    name = parseData.get('name', [''])[0]
    status = parseData.get('status', [''])[0] if 'status' in parseData else None

    isExist = Category.query.filter_by(name=name).first()
    if isExist:
        return jsonify({'msg': 'Category already exists'}), 400
    
    insert = Category(name=name, status=status)
    try:
        db.session.add(insert)
        db.session.commit()
        return jsonify({'msg': 'Category saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/update/<int:id>', methods=['PUT'])
def updateRecord(id):
    data = request.form.get('data')
    parseData = parse_qs(data)
    name = parseData.get('name', [''])[0]
    status = parseData.get('status', [''])[0] if 'status' in parseData else None

    # Check if the category exists and is not the same as the updated category
    category = Category.query.filter(Category.id != id, Category.name == name).first()
    if category:
        return jsonify({'msg': 'Category already exists'}), 400

    # Retrieve the existing category by ID
    category = Category.query.get(id)
    if not category:
        return jsonify({'msg': 'Category does not exist'}), 404

    # Update the category details
    category.name = name
    category.status = status

    try:
        db.session.commit()
        return jsonify({'msg': 'Category updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
             <button type="button" onclick="editRecord({{id: '{row.id}', name: '{row.name}', status: '{row.status}'}})" class="text-base bg-gray-200 rounded-md text-xs w-7 h-7 me-1 dark:bg-gray-700 "><i class="fa-light fa-pen"></i></button>
             <button type="button" onclick="deleteRecord('{row.id}')" class="text-base bg-gray-200 rounded-md text-xs w-7 h-7 me-1 dark:bg-gray-700 "><i class="fa-light fa-trash"></i></button>
             ''',
             } 
            for row in rows]
        
    response = {'data': data}

    return jsonify(response)

# start 
if __name__ == '__main__':
    app.run(debug=True)

