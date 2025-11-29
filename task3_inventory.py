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


#function to generate report from inventory data
def generate_report(result):

    # gets the stock and prints the sum of all stock items
    stock = sum(item['stock'] for item in result)
    print(f"Total number of items in stock: {stock}")

    # Find the most expensive item
    most_expensive = max(result, key=lambda x: x['price'])
    print(f"Most expensive item: {most_expensive['name']} at ${most_expensive['price']}")


    # iterate through the inventory and print items that are out of stock
    for index in range(len(result)):
        item = result[index]
        if item['stock'] == 0:
            print(f"Item '{item['name']}' is out of stock.")


# function to restock an item given its product_id and amount to restock
def restock_item(result, product_id, amount):
    try:
        for item in result:
          if item['id'] == product_id:
             item['stock'] += amount
             print(f"Restocked '{item['name']}'. New stock: {item['stock']}")
    except:
        print(f"Item with ID {product_id} not found.")


# function to save the updated inventory back to the json file
def save_inventory(result):
    import json
    with open('inventory.json', 'w') as file:
        json.dump(result, file, indent=4)
    print("Inventory saved to 'inventory.json'.")

if __name__ == "__main__":
    result = load_inventory()
    generate_report(result)
    restock_item(result, 102, 5) 
    save_inventory(result)