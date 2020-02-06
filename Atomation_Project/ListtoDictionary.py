def addToInventory(inventory, addedItems):
    iCount = 0
    Items={}
    for i in addedItems:
        Items = {i: 0}
        if list(Items.keys())[0] in inventory:
            Items = {i: (inventory[i]+1)}
            inventory.update(Items)
        else:
            Items = {i: iCount+1}
            inventory.update(Items)
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby','dagger']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
