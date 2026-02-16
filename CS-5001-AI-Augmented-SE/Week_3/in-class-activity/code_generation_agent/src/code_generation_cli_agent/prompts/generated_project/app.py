from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# In-memory to-do storage
todos = [
    {"id": 1, "task": "Learn Flask", "completed": False},
    {"id": 2, "task": "Build To-do App", "completed": False}
]
next_id = 3

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add', methods=['POST'])
def add_todo():
    global next_id
    task = request.form.get('task')
    if task:
        todos.append({"id": next_id, "task": task, "completed": False})
        next_id += 1
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = True
            break
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)