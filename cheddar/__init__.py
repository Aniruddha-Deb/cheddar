from flask import Flask, session
from cheddar import api
from chess import Board

def create_app():
	app = Flask(__name__, static_url_path='', static_folder='static/')
	app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

	app.register_blueprint(api.bp)
	
	return app
