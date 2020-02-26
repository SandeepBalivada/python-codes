import csv

data = ["sandeep,balivada,rajam".split(","),
        "soujanya,dabbeeru,vizag".split(","),
        "dhanavath,hanumanth,matur".split(","),
        "keerthika,b,chennai".split(",")]

with open('new_names.csv','w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in data:
         csv_writer.writerow(line)

with open('new_names.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)
with open('new_names.csv','a') as csv_file:
        csv_writer = csv.writer(csv_file)
        #csv_writer.writerow("ankita,mohanty,rourkela".split(","))
        #csv_writer.writerow("sandeep,balivada,rajam".split(","))
        csv_writer.writerow("soujanya,dabbeeru,vizag".split(","))
with open('new_names.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)