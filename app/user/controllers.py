from flask import *
from sqlalchemy.exc import IntegrityError
from app import *
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .getInfo import *


mod_user = Blueprint('user', __name__)

# @mod_user.route('/', methods=['GET'])
# def home_page():
# 	return render_template('home.html')

@mod_user.route('/', methods=['GET'])
def login_page():
	return render_template('login1.html')

@mod_user.route('/home', methods=['GET'])
def home_page():
    return render_template('index.html')



@mod_user.route('/getinfo', methods=['POST'])
def gi():
    try:
        codeforces_id = request.form['codeforces_id']
        pg_no = request.form['pg_no']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    try:
        return jsonify(result=get_info(codeforces_id,pg_no),success=True)
    except IntegrityError as e:
        return jsonify(success=False, message="This username already exists"), 400

    return jsonify(success=True)
