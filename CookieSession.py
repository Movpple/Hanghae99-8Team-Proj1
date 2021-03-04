# from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, session
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client.VIIIProject
#
# app = Flask(__name__)
#
# app.secret_key = 'random String'
#
# ID = 'admin'
# PW = '1234'
#
# url_for('name of the function of the route','parameters (if required)')
#
# @app.route('/')
# def home():
#     if 'userID' in session:
#         return redirect(url_for('index'))
#     else:
#         return redirect(url_for('login'))
#
# @app.route('/signUp', methods=['GET','POST'])
# def signUp():
#     return render_template('signUp.html')
#
# @app.route('/cocktail', methods=['GET','POST'])
# def cocktail():
#     return render_template('cocktail.html')
#
# @app.route('/aboutUs', methods=['GET','POST'])
# def about_us():
#     return render_template('aboutUs.html')
#
# @app.route('/contactUs', methods=['GET','POST'])
# def contact_us():
#     return render_template('contactUs.html')
#
#
# @app.route('/index')
# def index():
#     return render_template('index.html', username = session.get("userID"))
#
# @app.route('/login')
# def login():
#     return render_template('login.html')
#
# @app.route('/logintest', methods=['GET','POST'])
# def login_test():
#     global ID,PW
#     if request.method == 'POST':
#         user = request.form['user']
#         password = request.form['password']
#     if ID == user and PW == password:
#         session['userID'] = user
#         return redirect(url_for("home"))
#     else:
#         return redirect(url_for("fail"))
#
# @app.route('/fail')
# def fail():
#     return '로그인 실패 테스트'
#
#
# @app.route('/logout')
# def logout():
#     session.pop('userID')
#     return redirect(url_for('home'))
#
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0',port=5000,debug=True)



# 여기 밑으로는 주석 / 참고용입니다.


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


