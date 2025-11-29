#LOAD inventory from json file and print in python dictionary format
def load_inventory():
    import json

    try: #try block to handle file not found error
        with open('inventory.json', 'r') as file: # Open the JSON file
            inventory = json.load(file) # Load the JSON data into a Python dictionary
            
            #print(json.dumps(inventory, indent=4))#print data
            return inventory  #returns data from inventory.json
    except FileNotFoundError:
        print("Error: The file 'inventory.json' was not found.")

result = load_inventory()
print(result)
