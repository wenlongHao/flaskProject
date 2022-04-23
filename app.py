# from flask import Flask, url_for, render_template, request
#
# app = Flask(__name__)
#
#
# # @app.route('/')
# # def hello_world():
# #     return 'Hello World!'
#
# from markupsafe import escape
# # @app.route("/<name>")
# # def hello(name):
# #     return f"Hello, {escape(name)}!"
#
#
# # @app.route('/')
# # def index():
# #     return 'Index Page'
#
#
# @app.route('/helloa')
# def helloa():
#     return 'Hello, World'
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'
#
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'
#
# @app.route('/')
# def index():
#     return 'index'
#
# @app.route('/login')
# def login():
#     return 'login'
#
# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
#
# # from flask import request
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         return do_the_login()
# #     else:
# #         return show_the_login_form()
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
#
# # 要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性:
# # searchword = request.args.get('key', '')
#
#
# from flask import request
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')
#     ...
# from werkzeug.utils import secure_filename
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
#     ...
#
# from flask import request
#
# @app.route('/')
# def index():
#     username = request.cookies.get('username')
#     # use cookies.get(key) instead of cookies[key] to not get a
#     # KeyError if the cookie is missing.
#
# from flask import make_response
#
# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp
#
# from flask import abort, redirect, url_for
#
# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404
#
# if __name__ == '__main__':
#     app.run()

#########################################################
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'