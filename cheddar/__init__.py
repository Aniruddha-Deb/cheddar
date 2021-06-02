from flask import Flask
from cheddar import api

def create_app():
	app = Flask(__name__)

	app.register_blueprint(api.bp)

	@app.route('/')
	def index():
		return 'Hello, World!'
	
	return app
