# ✅ Flask Todo App

A beautiful, fully-functional todo list built with Flask — perfect for learning!

## 🚀 How to Run

```bash
# 1. Create & activate virtual environment
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

# 2. Install Flask
pip install flask

# 3. Run the app
python app.py

# 4. Open browser at:
#    http://localhost:5000
```

## 📂 File Structure

```
flask-todo/
├── app.py                 # Flask routes & logic
├── templates/
│   └── index.html         # Jinja2 HTML template
└── README.md
```

## 🧠 Flask Concepts Demonstrated

| Feature | Where |
|---|---|
| `@app.route()` | All routes in `app.py` |
| `render_template()` | `index()` function |
| `request.form` | `add()` function |
| `redirect()` + `url_for()` | After add/toggle/delete |
| Dynamic routes `<int:id>` | `toggle()` and `delete()` |
| Jinja2 `{{ }}` variables | `index.html` |
| Jinja2 `{% for %}` loop | Todo list rendering |
| Jinja2 `{% if %}` condition | Done state, empty state |

## ✨ Features

- Add tasks with the input form
- Mark tasks as done/undone (click the circle)
- Delete tasks (click ×)
- Live progress bar + percentage
- Task stats (total / done / remaining)
