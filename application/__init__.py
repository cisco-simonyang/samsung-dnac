from flask import Flask, render_template
from application.config import configure_app

from application.home import home

app = Flask(__name__)
configure_app(app)

# @app.errorhandler(500)
# def internal_server_error(error):
#     # app.logger.error('Server Error: %s', (error))
#     return render_template('content.html', msg='HTTP 500')

# @app.errorhandler(Exception)
# def unhandled_exception(error):
#     # app.logger.error('Unhandled Exception: %s', (error))
#     return render_template('content.html', msg='HTTP 500: Exception')

app.register_blueprint(home)