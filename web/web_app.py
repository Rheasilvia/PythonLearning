from flask import Flask, render_template, request
from checker import check_logged_in
app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)


# @app.route('/')
def hello() -> str:
    return 'Hello world from flask'


@app.route('/')
@app.route('/entry')
def enrty_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to Flask',
                           the_body='hello world~')
@app.route('/page1')
@check_logged_in
def page1()->str:
    return 'this is page 1'



if __name__ == '__main__':
    app.run(debug=True)
