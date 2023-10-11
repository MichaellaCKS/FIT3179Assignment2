with open ("js/billionaires.csv" , "r") as f,open ("js/top5.csv" , "w") as o:
    for line in f:
        o.write(line)
        break
    for line in f:
        line = line.strip()
        line2 = line.split(",")
        country = line2[5]
        if country in ["United States" , "China", "India", "United Kingdom","Germany"]:
            line = line + '\n'
            o.write(line)

    
  