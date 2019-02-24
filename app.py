import datetime
import os
import json

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    query_results = []
    return_object = []
    qry = db_session.query(Items)
    query_results = qry.all()
    for item in query_results:
        return_object.append(item.serialize())
    return json.dumps(return_object,indent=4, separators=(',', ': '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
