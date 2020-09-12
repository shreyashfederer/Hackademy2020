Products = ["Chair","Samsung","Lays","Sanitizer","Clock","Table","Sony","Airpods","DELL"]
result = {}

def get_products(text):
  global Products
  for value in text:
       if(str(value.description) in Products):
           item = value.description
           prices = []
           y1 = value.bounding_poly.vertices[0].y
           y2 = value.bounding_poly.vertices[2].y
           print(type(y1))
           print(y1,y2)
           print("\n")
           for cmppoints in text:
               #print("TEST :({},{}) ".format(cmppoints.bounding_poly.vertices[0].y,cmppoints.bounding_poly.vertices[2].y))
               if(int(cmppoints.bounding_poly.vertices[0].y) in range(y1-20,y1+20) and cmppoints.bounding_poly.vertices[2].y in range(y2-20,y2+20)):
                   #print("Inside block: ")
                #    print(cmppoints['description'],ord(cmppoints['description'][0]))
                   #print("\n")
                #    print(type(cmppoints['description']))
                   #print(cmppoints.description[0])
                   if(ord(cmppoints.description[0]) in range(46,58)):
                       if(cmppoints.description.find('.') == -1):
                           prices.append(int(cmppoints.description))
                       else:
                           splitbydecimal = cmppoints.description.split(".")
                           prices.append(int(splitbydecimal[0].replace(",", "")))
           print(prices)    
           result[item] = max(prices)                    
  print("Output from get_products %s " % (result))                            
  return result