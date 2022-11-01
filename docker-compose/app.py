import redis

from flask import Flask

app = Flask(__name__)

@app.route('/add1/<field>/<nm>')
def add(field,nm):
    db = redis.Redis(host='redis1', port=6379)
    for i in range(min(nm, 1000)):
        db.incr('field')

    return 'field {} is equal to {} for add1\n'.format(field, db.get('field'))
    

@app.route('/add2/<field>/<nm>')
def add(field,nm):
    db = redis.Redis(host='redis2', port=6379)
    for i in range (min(nm, 1000)):
        db.incr('field')

    return 'field {} is equal to {} for add2\n'.format(field, db.get('field'))
    