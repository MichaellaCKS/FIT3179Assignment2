import math
country_dict = {
    "United States" : [0,0],
    "Germany" : [0,0],
    "China" : [0,0],
    "India" : [0,0],
    "United Kingdom" : [0,0]

}
with open ("js/billionaires.csv" , "r") as f,open ("js/top5.csv" , "w") as o:
    for line in f:
        line = line.strip()
        line2 = line.split(",")
        country = line2[5]
        gender = line2[13]
        if country in country_dict and gender == 'M':
            country_dict[country][0] += 1
        elif country in country_dict and gender == 'F':
            country_dict[country][1] += 1
    for country in country_dict.values():
        for i in range(len(country)):
            values = math.ceil(country[i] / 10)
            country[i] = values
    print(country_dict)
    for country in country_dict:
        for i in range(len(country_dict[country])):
            for j in range(country_dict[country][i]):
                if i == 0 :
                    line = country + "," + "M\n"
                    o.write(line)
                else:
                    line = country + "," + "F\n"
                    o.write(line)
        


    
  