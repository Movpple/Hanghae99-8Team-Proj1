from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, session
from pymongo import MongoClient
import hashlib
import jwt
import datetime

client = MongoClient('localhost', 27017)
db = client.VIIIProject

app = Flask(__name__)

secret_key = 'VIII for liquor'


# url_for('name of the function of the route','parameters (if required)')

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, secret_key, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('index.html', user=user_info["id"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/signUp', methods=['GET','POST'])
def signUp():
    return render_template('signUp.html')

@app.route('/api/signUp', methods=['POST'])
def api_signUp():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    email_receive = request.form['email_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'email': email_receive})

    return jsonify({'result': 'success'})




@app.route('/cocktail', methods=['GET','POST'])
def cocktail():
    return render_template('cocktail.html')

@app.route('/aboutUs', methods=['GET','POST'])
def about_us():
    return render_template('aboutUs.html')

@app.route('/contactUs', methods=['GET','POST'])
def contact_us():
    return render_template('contactUs.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60)
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    print(username_receive)
    exists = bool(db.user.find_one({'id': username_receive}))
    print(exists)
    return jsonify({'result': 'success', 'exists': exists})

@app.route('/searchPage')
def search():
    return render_template('search.html')

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('mytoken', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)







#request 참고용

# @app.route('/test', methods=['GET'])
# def test_get():
#     title_receive = request.args.get('title_give')
#     print(title_receive)
#     return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
#
# @app.route('/test', methods=['POST'])
# def test_post():
#     title_receive = request.form['title_give']
#     print(title_receive)
#     return jsonify({'result':'success', 'msg': '이 요청은 POST!'})



## request + Jinja 테스트 1번
# @app.route('/data', methods=['GET','POST'])
# def test():
#     if request.method == 'POST':
#         user_temp = request.form['user']
#         pass_temp = request.form['password']
#         print(user_temp,pass_temp)
#         return render_template('data.html', user=user_temp, password=pass_temp)
#     else:
#         user_temp = request.args.get('user')
#         pass_temp = request.args.get('passw')
#         print(user_temp,pass_temp)
#         return render_template('index.html', user=user_temp, password=pass_temp)


### Cookie 참고용

# @app.route('/setcookie', methods = ['POST', 'GET'])
# def setcookie():
#     if request.method == 'POST':
#         user = request.form['user']
#         password = request.form['password']
#         resp = make_response("Cookie Setting Complete")
#         resp.set_cookie('userID', user)
#         resp.set_cookie('userPass', password)
#         return resp


# @app.route('/getcookie')
# def getcookie():
#     name = request.cookies.get('userID')
#     password= request.cookies.get('userPass')
#     return '<h1>welcome ' + name +' '+ password + '</h1>'


