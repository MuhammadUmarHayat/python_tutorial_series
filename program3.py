#match operator is used for decision making for a single variable
temp="Low" #Hign ,medium ,low
match temp:
    case "High":
        print("Today weather is hot")

    case "Medium":
        print("Weather is medium")
    case "Low":
        print ("Today weather is very cool")
    case _:
        print("Tempratue must be high,medium or low")
