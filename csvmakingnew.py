import csv
import panda as pd

mydict = {
    'name' : ["sandeep","soujanya","hanumanth","keerthi","ankitha"],
     'age' : [23,22,23,23,22],
     'city' : ["rajam","vizag","matur","chennai","rourkela"]
}

df = pd.DataFrame(mydict)
df.to_csv('csvexamplefile')
