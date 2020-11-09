import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
outerspace = client.outerspace
planets = outerspace.planets

planets.insert_one({'name': 'Earth', 'color': 'blue'})
planets.insert_many([{'name': 'Mars', 'color': 'red'},
                    {'name': 'Saturn', 'color': 'yellow'},
                    {'name': 'Pluto', 'color': 'brown'}],)
for planet in planets.find({}):

    print(planet)

planets.update_one({'name' : 'Earth'}, {'$set': {'moons': 1}})
planets.update_one({'name' : 'Mars'}, {'$set': {'moons': 2}})
planets.update_one({'name' : 'Saturn'}, {'$set': {'moons': 62}})
planets.update_one({'name' : 'Pluto'}, {'$set': {'moons': 5}})

planets.delete_one({'name': 'Pluto'})

planets.find({'moons': {'$gt': 1, '$lt': 10}})
planets.find({'color': {'$nin': ['red', 'blue']}})
planets.find({'$nor': [{'color': 'yellow'}, {'name': 'Mars'}]})
planets.find({'color': {'$not': {'$eq': 'blue'}}})
planets.find({'color': {'$ne': 'blue'}})
planets.find({'color': {'$nin': ['blue']}})