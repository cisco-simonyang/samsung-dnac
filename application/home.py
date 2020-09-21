
from flask import *
from application import dnac

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET'])
def _home():
	return render_template('login.html')


@home.route('/login', methods=['POST'])
def _login():
	print('login')

	ip = request.form.get('ip')
	username = request.form.get('username')
	password = request.form.get('password')
	token = dnac.login(ip, username, password)

	print('token: %s' % token)
	# print('%s %s %s' % (ip, user, password))
	# return render_template('clients.html')
	# return render_template('clients.html')
	response = make_response(redirect('/clients'))
    # response.set_cookie('auth_token', token)
	response.set_cookie('ip', ip)
	response.set_cookie('auth_token', token)
	return response



@home.route('/clients', methods=['GET'])
def _client():
	return render_template('clients.html')

# @home.route('/', methods=['GET'])
# def home():
# 	# return render_template('login.html', msg=salutation)
# 	return render_template('login.html')


@home.route('/api/clients', methods=['GET'])
def _api_clients():
	ip = request.cookies.get('ip')
	token = request.cookies.get('auth_token')
	res = dnac.get_clients(ip, token)
	return res


@home.route('/print/<input>', methods=['GET'])
def print_url_param(input=None):
	return jsonify(resp=input)
