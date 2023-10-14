category_list = ["Fashion & Retail","Automotive","Technology","Finance & Investments","Media & Entertainment","Telecom","Diversified","Food & Beverage","Logistics","Gambling & Casinos","Manufacturing","Real Estate","Metals & Mining","Energy","Healthcare","Service","Construction & Engineering","Sports"]
source_dict = {
    "root": ['', ''],
    "Fashion & Retail" : ['root', ''],
    "Automotive" : ['root', ''],
    "Technology" : ['root', ''],
    "Finance & Investments" : ['root', ''],
    "Media & Entertainment" : ['root', ''],
    "Telecom" : ['root', ''],"Diversified" : ['root', ''],
    "Food & Beverage" : ['root', ''],
    "Logistics" : ['root', ''],
    "Gambling & Casinos" : ['root', ''],
    "Manufacturing" : ['root', ''],
    "Real Estate" : ['root', ''],
    "Metals & Mining" : ['root', ''],
    "Energy" : ['root', ''],
    "Healthcare" : ['root', ''],
    "Service" : ['root', ''],
    "Construction & Engineering" : ['root', ''],
    "Sports" : ['root', '']
}
with open ("js/billionaires_copy.csv") as f, open ("js/treemap.csv","w") as o:
    for line in f:
        line = line.strip()
        line = line.split(",")
        parent = line[2]
        amount = int(line[1])
        name = line[7]
        if name not in source_dict and amount > 5000:
            source_dict[name] = [parent,amount]
        elif name in source_dict and amount > 5000: 
            try:
                source_dict[name][1] += int(amount)
            except:
                pass
    for i in source_dict:
        o.write(i + "," + source_dict[i][0] + "," + str(source_dict[i][1]) + '\n')