from app import app
from flask import render_template

@app.route('/')
def index():
    
    context = {
        'users' : ["josh", "nisarg", "ken", "thomas"]
}

    return render_template("index.html", **context)

@app.route('/about')
def about():


    context = {
        'logged_in-user': 'Derek',
        'info_to_display' : 'This is flask'
}
    return render_template('about.hmtl')