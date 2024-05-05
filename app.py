from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pos')
def pos():
    return render_template('pos.html')

@app.route('/catalog/categories')
def categories():
    return render_template('catalog/categories.html')

if __name__ == '__main__':
    app.run(debug=True)
