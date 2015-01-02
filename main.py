__author__ = 'jms'


import mongodb as db
import process as pss
import analysis as an



def main():
    print ("Creando DB...")
    db.removeDB()
    db.createDB()

    print ("Procesando datos de producto...")
    pss.countProducts()

    print ("Procesando pares de productos...")
    pss.countPairsOfProducts()


    print ("="*80)
    for (i,j) in [(1,25),(1,50),(1,75),(5,50),(10,25),(20,25),(50,25)]:
        print ("Support:",i, "Condfidence:",j)
        an.analize(i,j)
        print ("-"*80)

if __name__ == "__main__":
    main()

