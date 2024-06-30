""""
    prg : Find The Vechicle Maillage
    author : bala
    created at : 30-06-2024
"""

import os

# application tittle

print("******************************************")
print("\tFind The Vechicle Maillage")
print("******************************************")

# getting the informations from end user

start_km = int(input("Enter the starting km :"))
end_km = int(input("Enter the ending km :"))
millage = int(input("Enter your vehicle millage :"))
fual_price = int(input("Enter your fual price :"))

# calculations 

total_km = end_km - start_km
fual_conception = round((total_km/millage),2)
total_fual_price = fual_conception * fual_price
print(fual_conception)

# result

os.system("cls")
print("******************************************")
print("\t\tYour Maillage")
print("******************************************")
print("Starting km       :"+str(start_km))
print("End km            :"+str(end_km))
print("Total km          :"+str(total_km))
print("Fual conception   :"+str(fual_conception))
print("Total fual price  :"+str(total_fual_price))
