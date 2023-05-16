
# 1

def readFromFile(spending):
    f = open("spending.csv", "r")
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    data = []

    for i in range(len(lines)):
        items = lines[i].split(",")
        date = items[0]
        product = items[1]
        amount = items[2]
        data.append((date, product, amount))

    return(data)

# print(readFromFile("spending.csv"))
    

# 2
# [("2021-11-22 03:54:32" , "Milk - Homo", 97.73), ("2021-11-21 01:24:00", "Scampi Tail", 61.83)]
def total(data):
    total = 0.0
    for i in range(len(data)):
        total = total + data[i][2]
    return total
            
print (total(data))

# 3

def daily(data):
    dates = []                                      # empty array
    for i in range(len(data)):                      
        date = data[i][0].split(" ")[0]             # removes space between time and date
        dates.append((date, data[i][2]))            # adds date and amount to empty array
    
    dates.sort(key=lambda x:x[0])
    

    d_dates = []
    d_amts = []
    current_date = ""
    index = -1
    for i in range(len(dates)):
        if current_date != dates[i][0]:             # if variable current_date not = to date
            d_dates.append(dates[i][0])             # add date to d_dates array
            d_amts.append(dates[i][1])              # add 
            current_date = dates[i][0]
            index = index + 1
        else:
            d_amts[index] = d_amts[index] + dates[i][1]

    result = []
    for i in range(len(d_dates)):
        result.append((d_dates[i], d_amts[i]))
    return result

print(daily("spending.csv"))
            
# ddates = [2021-11-22, 2021-11-23, 2021-11-24]
# damts = [27, 12, 15]
# [(2021-11-22, 12), (2021-11-22, 15), (2021-11-23, 12), (2021-11-24, 15)]


# 4
# [("2021-11-22 03:54:32" , "Milk - Homo", 97.73), ("2021-11-21 01:24:00", "Scampi Tail", 61.83)]
def productsOnDay(data, day):
    products = []
    for i in range(len(data)):
        if data[i][0].split(" ")[0] == day:                 # splits time from date == day
            if data[i][1] not in products:
                products.append(data[i][1])






 