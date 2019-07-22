from flask import Flask, escape, request, render_template

app = Flask(__name__)


# create some dummy data until we configure a database

posts = [
    {
        'author' : 'Ankan Basu',
        'title'  : "Learning Flask",
        'content' : "glad that I have used Sinatra before!",
        'date_posted': 'July 21, 2019'
    },

    {
        'author' : 'Mormi Basu',
        'title'  : "Using Flask",
        'content' : "Daddy is the best!",
        'date_posted': 'July 21, 2019'
    },

    {
        'author' : 'Mormi Basu',
        'title'  : "Using Flask",
        'content' : "Daddy is the best!",
        'date_posted': 'July 21, 2019'
    }


]



@app.route('/')
def hello():
    name = request.args.get("name", "World Yes")
    #return 'Hello'
    #return f'<h1>Hello, {escape(name)}!</h1>'
    return render_template('home.html') # render template us used to display a html file from templates folder

@app.route('/about')
def about():
    name = request.args.get("name", "About me")
    #return f'<h1>Hello, {escape(name)}!</h1>'
    return render_template('about.html', title='About the page')


@app.route('/posts')
def render_posts():
    ## render the template and pass the posts dictionary to the frontend
    return render_template('posts.html', posts=posts, title='Greatest Posts')


# export FLASK_APP=flaskblog.py
# export FLASK_DEBUG=1 ## this will auto refresh webserver.


if __name__=='__main__':
    app.run(debug=True)