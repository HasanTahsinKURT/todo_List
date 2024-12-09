from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/tahsin/Desktop/todo_List/todo.db'

db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)
    '''Todo example [{"id":1,"tittle":"First Attempt","content":"First Attempt Todo","complete":0}]'''
    
@app.route("/add", methods=["POST"])
def addTodo():
    tittle = request.form.get("tittle").strip()
    content = request.form.get("content").strip()

    # Eğer title veya content boşsa, hata mesajı döndür.
    if not tittle or not content:
        return "<script>alert('Title and Content cannot be empty!'); window.location.href = '/';</script>"

    # Eğer boş değilse yeni todo oluştur ve kaydet.
    newTodo = Todo(tittle=tittle, content=content, complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<string:id>")
def contentUpdate(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def todoDelete(id):
    todo = Todo.query.filter_by().first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/detail/<string:id>")
def detailTodo(id):
    todo = Todo.query.filter_by().first()

    return render_template("detail.html", todo=todo)


class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tittle = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)


if __name__ == '__main__':
    app.run(debug=True)




'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
'''
