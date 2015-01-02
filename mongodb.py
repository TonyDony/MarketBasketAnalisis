__author__ = 'jms'


import csv
from pymongo import MongoClient, Connection


def createDB():
    conn = MongoClient()

    db = conn.marketBasket

    with open("groceries.csv", 'r') as basket:
        reader = csv.reader(basket)
        for row in reader:
            shopping = []
            for value in row:
                shopping.append(value)
            d = {}
            d['content'] = shopping
            db.baskets.insert(d)


def removeDB():
    c = Connection()
    c.drop_database('marketBasket')