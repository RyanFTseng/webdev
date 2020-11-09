import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

outerspace=client.outerspace
planets=outerspace.planets

client.drop_database(outerspace)

planets.insert_one({'name': 'Earth', 'color': 'blue'})
planets.insert_many([{'name': 'Mars', 'color': 'red'},
                     {'name': 'Saturn', 'color': 'yellow'},
                     {'name': 'Pluto', 'color': 'brown'}])

#planets.update_many([{'name': 'Earth'}, {'$set': {'moons': 1}},
#                     {'name': 'Mars'}, {'$set': {'moons': 2}},
#                     {'name': 'Saturn'}, {'$set': {'Moons':62}},
#                     {'name': 'Pluto'}, {'$set': {'Moons': 5}}])

planets.update_one({'name' : 'Earth'}, {'$set': {'moons': 1}})
planets.update_one({'name' : 'Mars'}, {'$set': {'moons': 2}})
planets.update_one({'name' : 'Saturn'}, {'$set': {'moons': 62}})
planets.update_one({'name' : 'Pluto'}, {'$set': {'moons': 5}})

planets.delete_one({'name' : 'Pluto'})


#for planet in planets.find({}):
  #  print(planet)


#for planet in planets.find({'moons':{'$gt':1,'$lt':10}}):
#    print(planet)

#for planet in planets.find({'color':{'$nin':['red','blue']}}):
#    print(planet)

#for planet in planets.find({'$nor':[{'color':'yellow'}, {'name':'Mars'}]}):
#    print(planet)

for planet in planets.find({'color':{'$not':{'$eq':'blue'}}}):
    print(planet)
