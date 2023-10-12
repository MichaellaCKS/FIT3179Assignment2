category_dict = dict()
with open ("js/billionaires.csv" , "r") as f,open ("js/bubble.csv" , "w") as o:
    for line in f:
        line = line.strip()
        line2 = line.split(",")
        category = line2[2]
        if category not in category_dict and category != "category":
            category_dict[category] = 0
with open ("js/billionaires.csv" , "r") as f,open ("js/bubble.csv" , "w") as o:
    for line in f:
        line = line.strip()
        line2 = line.split(",")
        category = line2[2]
        worth = line2[1]
        if category != "category":
            category_dict[category] += int(worth)
    for i in category_dict:
        line = str(i)+","+str(category_dict[i])+'\n'
        o.write(line)

