from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data
TASKS = [
    {'id': 1, 'title': 'Learn Flask Routing', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build Beautiful To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push project to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

@app.route('/')
def index():
    total = len(TASKS)
    completed = len([t for t in TASKS if t['status'] == 'Completed'])
    pending = total - completed
    return render_template('index.html',
                           tasks=TASKS,
                           total=total,
                           completed=completed,
                           pending=pending)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        priority = request.form.get('priority')

        if title:
            new_id = max([t['id'] for t in TASKS], default=0) + 1
            TASKS.append({
                'id': new_id,
                'title': title.strip(),
                'status': 'Pending',
                'priority': priority
            })
            return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    if not task:
        return "Task not found", 404
    return render_template('task.html', task=task)

@app.route('/toggle/<int:id>')
def toggle_status(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    if task:
        task['status'] = 'Completed' if task['status'] != 'Completed' else 'Pending'
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)