from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World Yes")
    #return 'Hello'
    return f'<h1>Hello, {escape(name)}!</h1>'

@app.route('/about')
def about():
    name = request.args.get("name", "About me")
    #return 'Hello'
    return f'<h1>Hello, {escape(name)}!</h1>'


# export FLASK_APP=flaskblog.py
# export FLASK_DEBUG=1 ## this will auto refresh webserver.


if __name__=='__main__':
    app.run(debug=True)