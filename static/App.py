from flask import Flask,render_template

app = Flask(__name__,template_folder='../Template')

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/pro')
def pro():
    return 'Products'

if __name__== "__main__":
    app.run(debug=True)