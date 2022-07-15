from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html', dojos=Dojo.get_all())

@app.route('/dojo/create', methods=['POST'])
def createDojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojo/show')

@app.route('/dojo/show/<int:id>')
def show(id):
    data={ 'id' : id }
    dojo=Dojo.get_join(data)
    return render_template('show.html', dojo=dojo)