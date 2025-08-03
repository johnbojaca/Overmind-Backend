from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/overminddb'
mongo = PyMongo(app)

db = mongo.db

@app.route('/insurance', methods=['GET'])
def getInsurances():
    insurances = []
    for insurance in db.insurances.find():
        insurances.append({
            '_id': str(ObjectId(insurance['_id'])),
            'name': insurance['name'],
            'description': insurance['description'],
            'insurance_type': insurance['insurance_type'],
            'benefits': insurance['benefits'],
            'value': insurance['value'],
            'image': insurance['image']
        })
    return insurances

if __name__ == "__main__":
    app.run(debug=True)