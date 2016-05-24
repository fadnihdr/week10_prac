#create a new type of exception
class Low_Inventory_Exception(Exception):
    def __init__(self):
        print("The inventory is low!")

def test():
    inventory = 11
    if inventory < 10:
        raise Low_Inventory_Exception

try:
    test()
except(Low_Inventory_Exception):
    print("Something is not right.")
else:
    print("Everything is good.")
finally:
    print("Everything is fixed.")