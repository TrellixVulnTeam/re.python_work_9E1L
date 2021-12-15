from flask import  Flask,request,render_template

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',tanchu = '')

@app.route('/timetable',methods=['GET','POST'])
def timetable():
    password = '123456'
    user = {
        'tongding' : {
            'mon1': 'python语言',
            'mon2':'python语言',
            'mon3': 'python语言',
            'mon4': '',
            'mon5': '',
            'mon6': '',
            'mon7': '',
            'mon8': '',
            'mon9': '',
            'mon10': '',
            'mon11': '',
            'mon12': '',
            'mon13': '',
            'mon14': '',
            'mon15': '',
            'tue1': '',
            'tue2': '',
            'tue3': '',
            'tue4': '',
            'tue5': '',
            'tue6': '',
            'tue7': '',
            'tue8': '',
            'tue9': '',
            'tue10': '基础治学',
            'tue11': '基础治学',
            'tue12': '基础治学',
            'tue13': '',
            'tue14': '',
            'tue15': '',
            'wed1': '',
            'wed2': '',
            'wed3': '融合新闻学',
            'wed4': '融合新闻学',
            'wed5': '融合新闻学',
            'wed6': '',
            'wed7': '',
            'wed8': '',
            'wed9': '',
            'wed10': '',
            'wed11': '',
            'wed12': '',
            'wed13': '',
            'wed14': '',
            'wed15': '',
            'thu1': '',
            'thu2': '',
            'thu3': '',
            'thu4': '',
            'thu5': '',
            'thu6': '',
            'thu7': '',
            'thu8': '',
            'thu9': '',
            'thu10': '',
            'thu11': '',
            'thu12': '',
            'thu13': '',
            'thu14': '',
            'thu15': '',
            'fri1': '',
            'fri2': '',
            'fri3': '',
            'fri4': '',
            'fri5': '',
            'fri6': '',
            'fri7': '',
            'fri8': '',
            'fri9': '',
            'fri10': '',
            'fri11': '',
            'fri12': '',
            'fri13': '',
            'fri14': '',
            'fri15': '',
            'password':'123456'
        },
        'twodog' : {
            'mon1': '',
            'mon2': '',
            'mon3': '',
            'mon4': '',
            'mon5': '',
            'mon6': '',
            'mon7': '',
            'mon8': '',
            'mon9': '',
            'mon10': '',
            'mon11': '',
            'mon12': '',
            'mon13': '',
            'mon14': '',
            'mon15': '',
            'tue1': '',
            'tue2': '',
            'tue3': '',
            'tue4': '',
            'tue5': '',
            'tue6': '',
            'tue7': '',
            'tue8': '',
            'tue9': '',
            'tue10': '',
            'tue11': '',
            'tue12': '',
            'tue13': '',
            'tue14': '',
            'tue15': '',
            'wed1': '',
            'wed2': '',
            'wed3': '',
            'wed4': '',
            'wed5': '',
            'wed6': '',
            'wed7': '',
            'wed8': '',
            'wed9': '',
            'wed10': '',
            'wed11': '',
            'wed12': '影视剧本写作',
            'wed13': '影视剧本写作',
            'wed14': '',
            'wed15': '',
            'thu1': '',
            'thu2': '',
            'thu3': '',
            'thu4': '演讲与口才',
            'thu5': '演讲与口才',
            'thu6': '',
            'thu7': '',
            'thu8': '',
            'thu9': '',
            'thu10': '',
            'thu11': '',
            'thu12': '',
            'thu13': '',
            'thu14': '',
            'thu15': '',
            'fri1': '',
            'fri2': '',
            'fri3': '',
            'fri4': '',
            'fri5': '',
            'fri6': '',
            'fri7': '',
            'fri8': '',
            'fri9': '',
            'fri10': '',
            'fri11': '',
            'fri12': '',
            'fri13': '',
            'fri14': '',
            'fri15': '',
            'password': '123456'
        }

    }
    if request.form['username']not in user.keys() or request.form['password']!= user[request.form['username']]['password']:
        tanchu = "true" #当tanchu = ‘true’时，会弹出alert提示密码错误
        return render_template('index.html',tanchu = tanchu)
    elif request.form['username'] in user.keys() and request.form['password'] ==  user[request.form['username']]['password']:
        username = request.form['username']
        return render_template('timetable.html',user = user[username] )

if __name__ == '__main__':
    app.run()