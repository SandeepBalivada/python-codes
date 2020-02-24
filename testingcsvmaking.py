import csv

def csv_writer(data,path):
    with open(path,"wb") as csv_file:
    writer = csv.writer(csv_file,delimiter=',')
    for line in data :
    writer.writerow(line)



if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "sandeep,balivada,rajam".split(","),
            "soujanya,dabbeeru,vizsg".split(","),
            "hanumanth,dhanavath,matur".split(",")
            ]
    path = "I:\output.csv"

    csv_writer(data,path)
    #print("This is what I want you to print now for checking")
