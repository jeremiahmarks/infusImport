from ISTables import tables
import ISServer
import my_pw

def main(athome=False):
    filename=''
    if athome:
        filename="/home/jlmarks/infusImport/"
    filename = filename + "fileout.txt"
    pp=open(filename, 'w')
    a=ISServer.newserver(my_pw.passwords['appname'],my_pw.passwords['apikey'])
    a.verifyConnection()
    b={}
    for eachtable in tables.keys():
        print eachtable
        pp.write("\n\n\t\t"+str(eachtable) +"\n\n")
        b[eachtable]=a.getAllRecords(eachtable, tables[eachtable])
        for eachitem in b[eachtable]:
            pp.write("  " + str(eachitem) + "\n")
    pp.close()
    return b

if __name__ == '__main__':
    main()