

Products = ["Chair","Samsung","Lays","Sanitizer","Clock","Table","Sony","Airpods"]

result = {}

categories = ["Electronics","Food","Apparels","Furniture","HomeItems"]

ElectronicsItems = ['Samsung',"Mobile","Airpods"]
Furniture = ["Table","Chair","Clock"]
Food = ["Lays"]
Apparels = ["Jeans","Shirt"]
HomeItems = ["Sanitizer"]



Spending = {


"Electronics" : 0,
"Furniture": 0,
"Food": 0,
"Clothing" : 0,
"Healthcare" : 0,
"HomeItems": 0,
"Other": 0


}


ResultSpending = {}

def CategorizeElement(result):

    for (product,price) in result.items():
        if product in ElectronicsItems :
            Spending['Electronics'] += int(price)
        elif product in Furniture:
            Spending['Furniture'] += int(price)
        elif product in Food:
            Spending['Food'] += int(price)
        elif product in Apparels:
            Spending['Food'] += int(price)
        elif product in HomeItems:
            Spending['HomeItems'] += int(price)        

        else:
            Spending['Other'] += int(price)
    for (product,price) in Spending.items():
    
        if price>0:
            ResultSpending[product] = price
         
    
    return ResultSpending
