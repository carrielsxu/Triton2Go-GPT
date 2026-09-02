def hasAllergy(ratemyfood,food_unique):
    allergy = (input("Are you allergic to any? please type: dairy/ eggs / gluten / soy / wheat / sesame / fish/ vegetarian/ vegan/ no?")).lower()
    for index, row in food_unique.iterrows():
        name = row["Name"]
        if name in ratemyfood:
            if row["Allergy: dairy?"] == "yes" and allergy == "dairy":
                del ratemyfood[name]
            if row["Allergy: eggs?"]  == "yes" and allergy == "egg":
                del ratemyfood[name]
            if row["Allergy: gluten?"]  == "yes" and allergy == "gluten":
                del ratemyfood[name]
            if row["Allergy: soy?"]  == "yes" and allergy == "soy":
                del ratemyfood[name]
            if row["Allergy: wheat?"]  == "yes" and allergy == "wheat":
                del ratemyfood[name]
            if row["Allergy: sesame?"]  == "yes" and allergy == "sesame":
                del ratemyfood[name]
            if row["Allergy: fish?"] == "yes" and allergy == "fish":
                del ratemyfood[name]
            if row["Vegetarian?"] == "yes" and allergy == "vegetarian":
                del ratemyfood[name]
            if row["Vegan?"] == "yes" and allergy == "vegan":
                del ratemyfood[name]
            else: 
                continue

def wantcalories(ratemyfood,food_unique):
    calorieschoice = (input("Do you want high calories? yes/no: ")).lower()
    calorieslist = [] 
    if calorieschoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_calories = -1
            highest_food = " "
            for index, row in food_unique.iterrows():
                if row["Name"] not in calorieslist and row["Name"] in ratemyfood:
                    if int(row["Calories"]) >= highest_calories:
                        highest_calories = int(row["Calories"])
                        highest_food = row["Name"]
            calorieslist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantfat(ratemyfood,food_unique):
    Fatchoice = (input("Do you want high fat? yes/no: ")).lower()
    Fatlist = [] 
    if Fatchoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_fats = -1
            highest_food = " "
            for index, row in food_unique.iterrows():
                if row["Name"] not in Fatlist and row["Name"] in ratemyfood:
                    if int(row["Fat"]) >= highest_fats:
                        Fates = int(row["Fat"])
                        highest_food = row["Name"]
            Fatlist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantCholesterol(ratemyfood,food_unique):
    Cholesterolchoice = (input("Do you want high Cholesterol? yes/no: ")).lower()
    Cholesterollist = [] 
    if Cholesterolchoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_Cholesterol = -1
            highest_food = " "
            for index, row in food_unique.iterrows():
                if row["Name"] not in Cholesterollist and row["Name"] in ratemyfood:
                    if int(row["Cholesterol"]) >= highest_Cholesterol:
                        Cholesterol = int(row["Cholesterol"])
                        highest_food = row["Name"]
            Cholesterollist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantSodium(ratemyfood,food_unique):
    Sodiumchoice = (input("Do you want high Sodium? yes/no: ")).lower()
    Sodiumlist = [] 
    if Sodiumchoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_Sodium = -1
            highest_food = " "
            for index, row in food_unique.iterrows():
                if row["Name"] not in Sodiumlist and row["Name"] in ratemyfood:
                    if int(row["Sodium"]) >= highest_Sodium:
                        highest_Sodium = int(row["Sodium"])
                        highest_food = row["Name"]
            Sodiumlist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantCarbs(ratemyfood,food_unique):
    Carbschoice = (input("Do you want high Carbs? yes/no: ")).lower()
    Carbslist = [] 
    if Carbschoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_Carbs = -1
            highest_food = " "
            for index, row in food_unique.iterrows():
                if row["Name"] not in Carbslist and row["Name"] in ratemyfood:
                    if int(row["Carbs"]) >= highest_Carbs:
                        highest_Carbs = int(row["Carbs"])
                        highest_food = row["Name"]
            Carbslist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantFiber(ratemyfood,food_unique):
    Fiberchoice = (input("Do you want high Fiber? yes/no: ")).lower()
    Fiberlist = [] 
    if Fiberchoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_Fibers = -1
            highest_food = " " 
            for index, row in food_unique.iterrows():
                if row["Name"] not in Fiberlist and row["Name"] in ratemyfood:
                    if int(row["Fiber"]) >= highest_Fibers:
                        highest_Fibers = int(row["Fiber"])
                        highest_food = row["Name"]
            Fiberlist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantSugar(ratemyfood,food_unique):
    Sugarchoice = (input("Do you want high Sugar? yes/no: ")).lower()
    Sugarlist = [] 
    if Sugarchoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_Sugar = -1
            highest_food = " " 
            for index, row in food_unique.iterrows():
                if row["Name"] not in Sugarlist and row["Name"] in ratemyfood:
                    if int(row["Sugar"]) >= highest_Sugar:
                        highest_Sugar = int(row["Sugar"])
                        highest_food = row["Name"]
            Sugarlist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood

def wantprotein(ratemyfood,food_unique):
    proteinchoice = (input("Do you want high protein? yes/no: ")).lower()
    Proteinlist = [] 
    if proteinchoice == "yes":
        score = len(ratemyfood)
        while score > 0:
            highest_protein = -1
            highest_food = " "
            for index, row in food_unique.iterrows():
                if row["Name"] not in Proteinlist and row["Name"] in ratemyfood:
                    if int(row["Protein"]) >= highest_protein:
                        highest_protein = int(row["Protein"])
                        highest_food = row["Name"]
            Proteinlist.append(highest_food)
            ratemyfood[highest_food] += score
            score -= 1
    return ratemyfood