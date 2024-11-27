def data_maker(captials): 
    city = []
    country = []

    for i in range(len(capital)): 
        if i % 2 == 0: 
            city.append(capitals[i])
        else: 
            country.append(capitals[i])

    return city, country 


# grade 11 method 
for i in range(len(country)-1): 
    current_country = country[i]
    track = i 

    for j in range(i+1, len(country)): 
        if country[j] < current_country: 
            current_country = country[j]
            track = j 


    temp = country[track]
    country[track] = country[i]
    country[i] = temp

    temp = city[track]
    city[track] = city[i]
    city[i] = temp 


#grade 12 method 

a_dict = {}

for i in range(country): 
    c = country[i]
    a_dict[c] = city[i]
country = sorted(country)
city = []

for value in country: 
    city.append(a_dict[value])