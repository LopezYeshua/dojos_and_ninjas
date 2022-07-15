from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create/ninjas', methods=['POST'])
def createNinja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/dojo/show/' + request.form['dojo_id'])

@app.route('/new_ninja')
def newNinja():
    return render_template('ninjas.html', dojos=Dojo.get_all())