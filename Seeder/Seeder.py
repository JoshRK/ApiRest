from pymongo import MongoClient

#réseau 'mynet2'
client = MongoClient(host="mongodb")


db = client["patients_db"]


patients_coll = db["patients"]


patients_data = [
    {"nom": "Doe", "prenom": "John", "ssn": "112345678901234"},
    {"nom": "Smith", "prenom": "Jane", "ssn": "223456789012345"},
    {"nom": "Johnson", "prenom": "Mary", "ssn": "334567890123456"}
]

#insertoin
patients_coll.insert_many(patients_data)

#Vérif
for patient in patients_coll.find():
    print(patient)
