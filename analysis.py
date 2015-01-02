__author__ = 'jms'

from pymongo import MongoClient

def analize(s,c):
    conn = MongoClient()
    db = conn.marketBasket

    s = int (s/100.0 * db.baskets.count())
    c = c/100.0

    counts = db.counts.find()

    supports = {}


    for doc in counts:
        if doc["value"] >= s:
            supports[doc["_id"]] = int(doc["value"])



    counter = 0
    pairs = db.pairCounts.find()

    printProducts = True
    for doc in pairs:
        name = (str(doc["_id"]).split(','))
        if  (name[0] in supports) and c <= (doc["value"]/supports[name[0]]):
            if printProducts:
                print ("Rules:")
                printProducts = False;
            counter += 1
            print (name[0]+"   "+ name[1])

    print ("Number of rules:", counter)






