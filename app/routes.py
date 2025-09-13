from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

tasks = []

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('main.index'))
    return render_template('index.html', tasks=tasks)

