#!/usr/bin/python
'''
obtendran datos de del vocabulario aleman
'''



def reader(file):
    try:
        dic = dict()
        f = open(file,"r")
        for line in f:
            text = line.split("=")                  # [aleman, espanol]
            dic[text[1][1:-1]] = text[0][:-1].upper()  #{"espanol": "Aleman"}

        f.close()
        return dic
    except FileExistsError:
        print("no existe")


#
#reader("pruba.txt")
