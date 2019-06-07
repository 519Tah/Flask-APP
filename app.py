from flask import Flask
from flask import render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Safiullah Taher',
        'title' : 'Blog Post1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog Post1',
        'content' : 'Second post content',
        'date_posted' : 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def aboutpage():
    return render_template('about.html', title='About')
    
    
    

if __name__ == "__main__":
    app.run(debug=True)
    