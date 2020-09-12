Products = ["Chair","Samsung","Lays","Sanitizer","Clock","Table","Sony","Airpods","DELL"]
result = {}

def get_products(text):
  global Products

  for value in text:
       if(str(value.description) in Products):

        #    print(value['boundingPoly'])
        #    print("\n")
           item = value.description
           prices = []

           #print(type(value['boundingPoly']))
           for vertices in value.bounding_poly.vertices:




            #    print(points)
            #    print(points[0]['y'])
            #    print(points[2]['y'])
               y1 = vertices[0].y
               y2 = vertices[2].y
               print(y1 + "" + y2 + "################################################")
               print("\n")
               for cmppoints in value:
                   if(cmppoints.bounding_poly.vertices[0]['y'] in range(y1-20,y1+20) and cmppoints.bounding_poly['vertices'][2]['y'] in range(y2-20,y2+20)):
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

                       else:
                           if(cmppoints['description']!=item):
                               item+= "_"+cmppoints['description']

                           
                           
                           
               print(prices)    
               print("\n")
               result[item] = max(prices) 
                  
                            
  print("Output from get_products %s " % (result))                            
  return result




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
