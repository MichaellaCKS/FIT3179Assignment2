country_dict = dict()


with open ("js/billionaires.csv", "r") as file_content, open('output.csv', 'w') as output_file:
    for line in file_content:
        line = line.strip()
        my_list = line.split(",")
        pays = my_list[5]
        if pays not in country_dict and pays!= "country":
            country_dict[pays] = 1

        elif  pays in country_dict and pays!= "country":
            country_dict[pays] += 1
    for i in country_dict:
        line = str(i) + ',' + str(country_dict[i]) + '\n'
        output_file.write(line)