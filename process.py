__author__ = 'jms'

from pymongo import MongoClient
from bson.code import Code




def countProducts():
    conn = MongoClient()

    db = conn.marketBasket


    mapper = Code("""
        function() {
            for (var i = 0; i < this.content.length; i++){
                emit(this.content[i],1);
            }
        }
        """)


    reducer = Code("""
        function(key, values){
            var total = 0;
            for (var i = 0; i < values.length; ++i){
                total = total + values[i];
            }
            return total;
        }
        """)

    db.baskets.map_reduce(mapper, reducer, "counts")

def countPairsOfProducts():
    conn = MongoClient()

    db = conn.marketBasket

    mapper = Code("""
        function() {
            for (var i = 0; i < this.content.length; i++){
                for (var j = 0; j < this.content.length; j++){
                    if(i!=j) {
                        emit(this.content[i]+','+this.content[j],1);
                    }
                }
            }
        }
        """)


    reducer = Code("""
        function(key, values){
            var total = 0;
            for (var i = 0; i < values.length; ++i){
                total = total + values[i];
            }
            return total
        }
        """)

    db.baskets.map_reduce(mapper, reducer, "pairCounts")
