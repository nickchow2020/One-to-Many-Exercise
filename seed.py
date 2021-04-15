from models import User,db ,Post
from app import app 

db.drop_all()
db.create_all() 

User.query.delete()

shumin = User(first_name='shumin',last_name='zhou',image_url='https://pickaface.net/gallery/avatar/9036435260091952bdb.png')
nick = User(first_name="nick",last_name='zhou',image_url='https://pickaface.net/gallery/avatar/20150418_075523_3821_t_pain.png')
stephen = User(first_name='stephen',last_name='zhou',image_url='https://pickaface.net/gallery/avatar/74841945_161206_2228_2op3n44.png')

post1 = Post(title="hello,world",content="I Love this world",user_id=1)
post2 = Post(title="I love you",content="I Love this hope",user_id=2)
post3 = Post(title="I love you too",content="I Love this too",user_id=3)

db.session.add(shumin)
db.session.add(nick)
db.session.add(stephen)

db.session.commit()

db.session.add(post1)
db.session.add(post2)
db.session.add(post3)

db.session.commit()