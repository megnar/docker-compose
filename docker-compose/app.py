import redis

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/add1/<field>')
def add1(field):
    db = redis.Redis(host='redis1', port=6379)
    db.incr('field')

    return 'field {} is equal to {} for add1\n'.format(field, db.get('field'))
    

@app.route('/add2/<field>')
def add2(field):
    db = redis.Redis(host='redis2', port=6379)
    db.incr('field')

    return 'field {} is equal to {} for add2\n'.format(field, db.get('field'))
    
