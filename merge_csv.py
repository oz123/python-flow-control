"""
merge two csv files and return a joined value

The files look like:

$ head register_men.csv
Stadt,"Post-leitzahl 1)","Fläche in km2 2)",männlich
"Berlin, Stadt",10178,891.12,1755700
"Hamburg, Freie und Hansestadt",20038,755.3,886289
"München, Landeshauptstadt",80331,310.71,714112
"Köln, Stadt",50667,405.02,524790
"Frankfurt am Main, Stadt",60311,248.31,363754
"Stuttgart, Landeshauptstadt",70173,207.33,313295
"Düsseldorf, Stadt",40213,217.41,296231
"Dortmund, Stadt",44135,280.71,287897
"Essen, Stadt",45127,210.34,283065
$ head register_women.csv
Stadt,"Post-leitzahl 1)","Fläche in km2 2)",weiblich
"Berlin, Stadt",10178,891.12,1819130
"Hamburg, Freie und Hansestadt",20038,755.3,924149
"München, Landeshauptstadt",80331,310.71,750189
"Köln, Stadt",50667,405.02,551145
"Frankfurt am Main, Stadt",60311,248.31,372660
"Stuttgart, Landeshauptstadt",70173,207.33,314737
"Düsseldorf, Stadt",40213,217.41,316999
"Dortmund, Stadt",44135,280.71,297916
"Essen, Stadt",45127,210.34,300019

The script finds a city and returns the joined number of men and woman
"""

import csv

def city_population():
    cache = {}
    with open('register_men.csv') as m, open('register_women.csv') as w:
        men,  women = csv.reader(m), csv.reader(w)
        while True:
            next(men), next(women)
            city = (yield)
            print("Searcing for %s" % city)
            if city in cache:
                print(city," found in cache")
            else:
                for rw, rm in zip(men, women):
                    if city in rw[0]:
                        total = int(rw[-1]) + int(rm[-1])
                        cache[city] = total
            print("The total population of %s is %s" % (city, cache[city]))
            m.seek(0)
            w.seek(0)
