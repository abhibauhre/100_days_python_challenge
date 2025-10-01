capitals = {
    "uttar pradesh":"lucknow",
    "madhya pradesh":"bhopal",
    "uttarakhand":"dehradun"  
}

#nested list using dictionary
travel_location = {
    "uttar pradesh":["jhansi","agra","varanasi"],  
    "madhya pradesh":["seoni","pachmarhi","orchha"],  
    "uttarakhand":["mussoorie","kasol","nainital"]  
}

#print agra
print(travel_location["uttar pradesh"][1])#this method is used to print agra from nested list

nested_list = ["a","b",["c","d"]]
print(nested_list[2][1])#its print d from nested list

travel_log = {
    "uttarpradesh":{
        "cities visited":["jhansi","delhi","mauranipur"],
        "num of visited": 12
    }, 
    "madhya pradesh": {
        "cities visited": ["seoni","bhopal","orchha"], 
        "num of visited": 8
    }
}
print(travel_log["madhya pradesh"]["cities visited"][1])#its print the value of bhopal from nested list