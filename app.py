# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "BASIT" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")

def web_1():
    name = "FIROZ" 
    age = "40" 
    
    return render_template('father.html', name = name, age = age)

# define the route to mother webpage
@app.route("/mother")
def web_2():
    name = "TABASSUM" 
    age = "36"
    
    return render_template('mother.html', name = name, age = age)

# define the route to friends webpage
@app.route("/friends")
def web_3():
    return "NO FRIENDS"

# add other routes, if you want
@app.route("/siblings")
def web_4():
    name = "SANA"
    age = "10"
    
    return render_template('siblings.html', name = name, age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
