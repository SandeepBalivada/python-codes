import csv

with open('csvfile','r') as new_file :
     csv_writer = csv.writer(new_file, delimiter=',')



     data = [ "firstname,lastname,city".split(","),
              "sandeep,balivada,rajam".split(","),
              "soujanya,dabbeeru,vizag".split(",")]

     for line in data:
       csv_writer.writerow(line)
