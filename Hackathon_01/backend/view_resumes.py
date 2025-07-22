from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['resume_db']
collection = db['resumes']

for r in collection.find():
    print("Name:", r.get('name', 'NA'))
    print("Email:", r.get('email', 'NA'))
    print("Phone:", r.get('phone', 'NA'))
    print("Skills:", r.get('skills', []))
    print("Text (truncated):", r.get('text', '')[:150])
    print("-" * 50)