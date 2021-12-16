from flask import Flask, render_template, redirect
from datetime import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap

from todo_form import TodoForm

csrf = CSRFProtect()
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'any code is availabe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////todo_list.db'
db = SQLAlchemy(app)
csrf.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(500), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, unique=True, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    end_date = db.Column(db.Date, nullable=False, unique=False)

    def __repr__(self):
        return '<Todo %r>' % self.title


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here

    form = TodoForm()
    if form.validate_on_submit():
        add_todo(form)
        return redirect('/')
    return render_template('index.html', form=form, entry_list=Todo.query.all())


def add_todo(form):
    todo_entry = Todo(title=form.data['title'], creation_date=dt.now(), end_date=form.data['end_date'], completed=False)
    db.session.add(todo_entry)
    db.session.commit()


@app.route('/delete/<int:id>')
def delete_todo(id):
    item = Todo.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:id>/<value>')
def completed_todo(id, value):
    item = Todo.query.get(id)
    print(item, item.completed,id)
    if value == 'True':
        item.completed = True
    else:
        item.completed=False
    db.session.commit()
    try:
        return redirect('/')
    except:
        print('exception')


# entry rtrieve show a list in website
if __name__ == '__main__':
    app.run()
