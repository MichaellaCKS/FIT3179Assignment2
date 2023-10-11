with open ("js/billionaires.csv" , "r") as f,open ("js/gender.csv" , "w") as o:
    male = 0
    female = 0
    for line in f:
        line = line.strip()
        line = line.split(",")
        gender = line[13]
        if gender == 'M':
            male += 1
        else:
            female += 1
    o.write("Gender,count\n")
    o.write("Male," + str(male)+ "\n")
    o.write("Female," + str(female)+ "\n")
    
