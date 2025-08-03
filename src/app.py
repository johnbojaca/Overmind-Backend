from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/overminddb'
mongo = PyMongo(app)

db = mongo.db

@app.route('/insurance_type', methods=['GET'])
def getInsuranceTypes():
    insurance_types = []
    for type in db.insurance_type.find():
        insurance_types.append({
            '_id': str(ObjectId(type['_id'])),
            'name': type['name'],
            'image': type['image']
        })
    return insurance_types

@app.route('/insurance/<id>', methods=['GET'])
def getInsurancesByTypeId(id):
    insurances = []
    for insurance in db.insurances.find( { "insurance_type": ObjectId(id) } ):
        insurances.append({
            '_id': str(ObjectId(insurance['_id'])),
            'name': insurance['name'],
            'description': insurance['description'],
            'benefits': insurance['benefits'],
            'insurance_type': str(ObjectId(insurance['insurance_type']))
        })
    return insurances

@app.route('/insurance', methods=['GET'])
def getInsurances():
    insurances = []
    for insurance in db.insurances.find():
        insurances.append({
            '_id': str(ObjectId(insurance['_id'])),
            'name': insurance['name'],
            'description': insurance['description'],
            'benefits': insurance['benefits']
        })
    return insurances

if __name__ == "__main__":
    app.run(debug=True)