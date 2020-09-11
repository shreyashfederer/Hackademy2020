# import bigjson

# with open('data.json', 'rb') as f:
#     j = bigjson.load(f)
#     print(j['cropHintsAnnotation'])
    

import json
f = open('data.json')
data = json.load(f)




f.close()




Products = ["Chair","Samsung","Lays","Sanitizer","Clock","Table","Sony","Airpods"]

result = {}

categories = ["Electronics","Food","Apparel","Furniture","HomeItems"]

ElectronicsItems = ['Samsung',"Mobile","Airpods"]
Furniture = ["Table","Chair","Clock"]
Food = ["Lays"]
Apparel = ["Jeans","Shirt"]
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

def CategorizeElement(result):

    for (product,price) in result.items():
        if product in ElectronicsItems :
            Spending['Electronics'] += int(price)
        elif product in Furniture:
            Spending['Furniture'] += int(price)
        elif product in Food:
            Spending['Food'] += int(price)
        elif product in Apparel:
            Spending['Food'] += int(price)
        elif product in HomeItems:
            Spending['HomeItems'] += int(price)        

        else:
            Spending['Other'] += int(price)




    return Spending


for (k, v) in data.items():
    
    if str(k)=="textAnnotations":
        for value in v:
            if type(value) == type(dict()):
               if(value['description'] in Products):

                #    print(value['boundingPoly'])
                #    print("\n")
                   item = value['description']
                   prices = []

                   #print(type(value['boundingPoly']))
                   for (newkey,points) in value['boundingPoly'].items():




                    #    print(points)
                    #    print(points[0]['y'])
                    #    print(points[2]['y'])
                       y1 = points[0]['y']
                       y2 = points[2]['y']
                       
                       print("\n")
                       for cmppoints in v:
                           if(cmppoints['boundingPoly']['vertices'][0]['y'] in range(y1-20,y1+20) and cmppoints['boundingPoly']['vertices'][2]['y'] in range(y2-20,y2+20)):
                            #    print("Inside block: ")
                            #    print(cmppoints['description'],ord(cmppoints['description'][0]))

                               print("\n")

                            #    print(type(cmppoints['description']))
                               if(ord(cmppoints['description'][0]) in range(46,58)):


                                   print("price: "+cmppoints['description'])

                                   if(cmppoints['description'].find('.') == -1):
                                       prices.append(int(cmppoints['description']))
                                   else:
                                       splitbydecimal = cmppoints['description'].split(".")
                                       prices.append(int(splitbydecimal[0].replace(",", "")))
                                    

                                   
                       print(prices)    
                       print("\n")
                       result[item] = max(prices) 
                        
                        
                            
print(result)
spendingpattern = CategorizeElement(result)

print(spendingpattern)








#    print("Key: " + k + "\n")
#    print("Value: " + str(v) + "\n")
    

        #print(type(v))
       

    #     #    print(str(value)+"\n")
    #     #    print(type(value))
    #        if type(value) == type(dict()):
    #            if(value['description'] == "Chair" or value['description']=="Samsung" or value['description']=="Lays"):
    #                print(value['boundingPoly'])
    #                print("\n")
    #                item = value['description']
    #                prices = []

    #                #print(type(value['boundingPoly']))
    #                for (newkey,points) in value['boundingPoly'].items():



    #                    print(points)
    #                    print(points[0]['y'])
    #                    print(points[2]['y'])
    #                    y1 = points[0]['y']
    #                    y2 = points[2]['y']
                       
    #                    print("\n")
    #                    for cmppoints in v:
    #                        if(cmppoints['boundingPoly']['vertices'][0]['y'] in range(y1-10,y1+10) and cmppoints['boundingPoly']['vertices'][2]['y'] in range(y2-10,y2+10)):
    #                         #    print("Inside block: ")
    #                         #    print(cmppoints['description'],ord(cmppoints['description'][0]))

    #                            print("\n")
    #                         #    print(type(cmppoints['description']))
    #                            if(ord(cmppoints['description'][0]) in range(46,58)):

    #                                print("price: "+cmppoints['description'])
    #                                prices.append(int(cmppoints['description']))
                           
    #                    result['item'] = max(prices) 
                        
                                        
    # print(result)


   
