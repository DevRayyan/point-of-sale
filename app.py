from flask import Flask,render_template,request


app = Flask(__name__)


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
    return render_template('catalog/categories.html')

# start 
if __name__ == '__main__':
    app.run(debug=True)
