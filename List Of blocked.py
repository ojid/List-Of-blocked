def animals():

    #----------------------------------
    #--------list of animals ----------
    #----------------------------------

    animals = ["Mallard","Hook Bill","African","Crested","Pilgrim","Toulouse", 
    "Blue Swedish","Roman Tufted","Steinbacher","Parrot","Swan","Eagle","Duck","Goose","Flamingo",
    "Penguin","Peacock","Owl","Hawk","Falcon"]
    
    #----------------------------------
    #-----list of blocked animals------
    #----------------------------------    

    block_animals = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    
    #----------------------------------
    #-----loop and if condition--------
    #----------------------------------
    
    for blocked in block_animals:
        if blocked in animals:
            animals.remove(blocked)

    #----------------------------------------------
    #-----return the animals list after remove-----
    #----------------------------------------------

    return animals

print(animals())