import os
from flask import Flask, request, make_response, jsonify
from chatbot.db import get_db
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='YOUR_SECRET_KEY',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    def results():
        req = request.get_json(force=True)
        action = req.get('queryResult').get('action')
        db = get_db()
        db.execute(
                    "INSERT INTO user (queryText, queryAction, params, fulfillmentText, intentMatched) VALUES (?,?,?,?,?)",
                    (req.get('queryResult').get('queryText'),
                    req.get('queryResult').get('action'),
                    req.get('queryResult').get('parameters').get('items'),
                    req.get('queryResult').get('fulfillmentText'),
                    req.get('queryResult').get('intent').get('displayName')),
                )
        db.commit()
        #db = get_db()
        #userQuery = db.execute(
        #            'SELECT queryText FROM user WHERE params = ?', (req.get('queryResult').get('parameters').get('items'),)
        #).fetchone()[0]
        #print (userQuery)
        #check platform 
        #return JSON which corresponds to the platform

        if(req.get('queryResult').get('parameters').get('items')=='phone'):
            return {
                "fulfillmentText":f"Ok I will help you in ordering a phone. :)"
            }
        elif (req.get('queryResult').get('parameters').get('items')=='earphones'):
            return {
                "fulfillmentText": f"OK I will help you in ordering earphones. :)"
            }
        else:
            return {'fulfillmentText': 'BEEP BOP BEEP!!!  '}

    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook():
        return make_response(jsonify(results()))
    
    from . import db
    db.init_app(app)

    def addData():
        req =  request.get_json(force=True)
        
        return 0

    def check():
        req =  request.get_json(force=True)
        
        return 0

    return app


