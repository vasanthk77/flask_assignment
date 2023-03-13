## 1 here import flask
from flask import Flask
##  2 here creating object
app=Flask(__name__)
## 3 creating the end point using routes and bind with functionality.....for backend
@app.route('/enter/<username>')
def show_user(username):
    return f'hello {username.upper()} !'
@app.route('/search')
def search_page():
    return "Welcome to the search page"
@app.route('/add')
def add_page():
    a=2
    b=3
    c=a+b
    return(str(c))


##  4running the application
if __name__=='__main__':
    app.run(debug=True)
