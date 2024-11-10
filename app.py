from flask import Flask,request,render_template
from datetime import datetime
app = Flask(__name__)

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

def datetime_format(value,format="%Y-%d-%m %H:%H"):
    return value.strftime(format)
app.add_template_filter(datetime_format,"dformat")

@app.route('/')
def hello_world():  # put application's code here
    user = User(username="haozhang", email="haozhang6868@163.com")
    return render_template('index.html',user=user)
@app.route('/filter')
def hello_filter():  # put application's code here
    user = User(username="haozhang", email="haozhang6868@163.com")
    mydatetime =datetime.now()
    return render_template('filter.html',user=user,mydatetime=mydatetime)
@app.route('/control')
def hello_control():
    age=17
    books = [{
        'name':"水浒",
        "author":"施耐庵"
    },
        {
            'name': "红楼",
            "author": "曹雪芹"
        },{
        'name':"西游记",
        "author":"吴承恩"
    },{
        'name':"三国",
        "author":"罗贯中"
    },{
        'name':"明朝那些事儿",
        "author":"当年明月"
    }    ]
    return render_template("control.html",age=age,books=books)
@app.route('/profile')
def hello_profile():
    return '个人主页'
@app.route('/blog/<int:blog_id>')
def hello_blog(blog_id):
    return render_template("blogdatil.html",blog_id=blog_id,username="zhanghao")
@app.route('/book/list')
def booklist():
    page = request.args.get("p",default=1,type=int)
    return f'您访问的是图书列表第页{page}的图书馆列表'
@app.route('/child')
def hellochild():
    return render_template("zimuban.html")
@app.route('/static')
def hellstatic():
    return render_template("static.html")
if __name__ == '__main__':
    app.run()
