# Reserved for splitting multiple packages

from application import app

if __name__ == '__main__':
	# app.run(debug=True)
	app.run(host='0.0.0.0')