from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def george():
    return render_template('george.html')


@app.route('/courses')
def show_courses():
    courses = [
        'ACCT 315',
        'ACCT 327',
        'MISY 350',
    ]
    return render_template('courses.html', courses=courses)


if __name__ == '__main__':
    app.run()
