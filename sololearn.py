# # 3 houses will give candy
# # 1 house toothbrush
# # 2 houses will give me doller bills
# # total = 6

# # 50 
# # 16.6667
# # 33.667


# houses = int(input("Enter the number houses visited: "))

# def dollar_chance(houses) :
#     dollar_bills = 2
#     total_items = houses
#     percentage = (dollar_bills / total_items ) * 100
#     percentage = round(percentage)
#     return percentage 
# result = dollar_chance(houses)
# print(f"The chances are {result}")



# houses = int(input())

# def dol(houses):
#     bills = 2
#     items = houses
    
#     if items == 0:
#         return "Cannot calculate percentage when the number of houses is zero."
    
#     perc = (bills / items) * 100
#     perc = round(perc)
#     return perc

# result = dol(houses)
# print(result)





# houses = int(input())

# def calculate_percentage_chance(total_houses_visited):
#     # Calculate the number of dollar bills and total number of items
#     number_of_dollar_bills = 2
#     total_items = total_houses_visited
    
#     # Calculate the percentage chance
#     percentage_chance = (number_of_dollar_bills / total_items) * 100
    
#     # Round up to the nearest whole number
#     percentage_chance = round(percentage_chance)
    
#     return percentage_chance

# # Calculate and print the percentage chance
# result = calculate_percentage_chance(houses)
# print(result)


# houses = int(input())

# def calculate_percentage_chance(total_houses_visited):
#     # Initialize the count of dollar bills and the total items
#     dollar_bills = 2
#     total_items = total_houses_visited - 3  # Subtract 3 for the non-candy houses
    
#     # Ensure there are at least three houses
#     if total_items >= 0:
#         # Calculate the percentage chance
#         percentage_chance = (dollar_bills / (total_items + 3)) * 100
        
#         # Round up to the nearest whole number
#         percentage_chance = round(percentage_chance)
#         return percentage_chance
#     else:
#         return "Invalid input: You must visit at least 3 houses."

# # Calculate and print the percentage chance
# result = calculate_percentage_chance(houses)
# print(result)

# houses = int(input())

# def calculate_percentage_chance(total_houses_visited):
#     # Calculate the percentage chance
#     dollar_bills = 2
#     total_items = total_houses_visited
    
#     if total_items >= 3:
#         percentage_chance = (dollar_bills / total_items) * 100
#         percentage_chance = round(percentage_chance)
#         return percentage_chance
#     else:
#         return "Invalid input: You must visit at least 3 houses."

# # Calculate and print the percentage chance
# result = calculate_percentage_chance(houses)
# print(result)

# import math
# houses = int(input())

# def calculate_percentage_chance(total_houses_visited):
#     # Calculate the percentage chance
#     dollar_bills = 2
#     total_items = 4  # Total items are fixed at 4 in this specific scenario
    
#     # Calculate the percentage chance
#     percentage_chance = (dollar_bills / total_items) * 100
#     percentage_chance = math.ceil(percentage_chance)
#     return percentage_chance

# # Calculate and print the percentage chance
# result = calculate_percentage_chance(houses)
# print(result)

# if team got over 10 Give a high five
# if dont move by atleast yard say shh
# if they move ten yard less say Ra for every yard they move 

#cheer creator

#solution 1 
# def cheer_event(dist):
#     if dist >=10 :
#         return "High five"
#     elif dist<1:
#         return "shh"
#     else :
#         return  "Ra!"  *  dist
    
# dist = int(input("Enter a distance: "))

# if 1 <= dist <= 10:
#     print(cheer_event(dist))
# else:
#     print("The distance should be between 1 and 10.")


# 2 sol

# x= int(input())  
# if x<1:
#     print("shh")
# elif x>10:
#      print("High Five")
# else:
#     while x>0:
#         print("Ra!", end = "")
#         x=x-1



# cost for paint is 40.00  canvas and brushes
# each color is 5.00
# tax 10%



#paint cost problem

# canvas_brushes_cost= 40.00
# paint = int(input()) 
# cost_paint = paint * 5.00
# tax = (canvas_brushes_cost + cost_paint ) * (10 / 100 )
# total_cost = canvas_brushes_cost + cost_paint + round(tax)
# print(total_cost)


# 2cents = 1 peso

# pesos_price = int(input("Enter the price in Pesos: "))
# dollars_price = int(input("Enter the price in Dollars: "))

# # peso = 2cents
# # 1dollar = 100 cents

# # 1 dollar = 50 peso



# # Convert the Dollars price to Pesos using the exchange rate (2 cents for every Peso)
# cents = dollars_price * 100

# if pesos_price < cents:
#     print("Pesos")
# else:
#     print("Dollars")

# Input prices in Pesos and Dollars
# price_in_pesos = int(input())
# price_in_dollars = int(input())

# cents = price_in_dollars * 100 
# print("price in cents",cents)
# peso = 2  * cents 
# print("Price in peso",peso)

# # Convert the price in Pesos to Dollars using the exchange rate
# price_in_pesos_in_dollars = price_in_pesos * 0.02

# # Compare the converted price with the price in Dollars
# if price_in_pesos_in_dollars < price_in_dollars:
#     print("Pesos")
# else:
#     print("Dollars")





price_in_pesos = int(input())
price_in_dollars = int(input())

#convert it
dollar_to_pesos =  price_in_pesos * 0.02




if dollar_to_pesos <= price_in_dollars :
    print("Pesos")
else:
    print("Dollars")




















