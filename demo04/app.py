from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)



HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "database_learn"
app.config['SQLALCHEMY_DATABASE_URI']=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)
#
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 12"))
#         print(rs.fetchone())
class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key = True,autoincrement = True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
with app.app_context():
    db.create_all()
    user1 = User(username="张三", password="1111")
    user2 = User(username="李四", password="2222")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/query')
def hello_query():
    user= User.query.get(2)
    print(f"{user.id}:{user.username}:{user.password}")# put application's code here
    return '数据查找成功!'
@app.route('/update')
def hello_update():
    user= User.query.filter_by(username = "张三").first()
    user.password = "155551675688"
    db.session.commit()
    return '数据更新成功!'

@app.route('/delete')
def hello_delete():

    User.query.filter(User.username == "李四").delete()
    db.session.commit()
    return '删除成功!'

if __name__ == '__main__':
    app.run()
