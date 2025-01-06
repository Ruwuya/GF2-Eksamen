# Program der tager et input og gemmer i en txt fil som herefter kan udskrives som tekst på skærmen

f = open("Database.txt", "a")
f.write(input("Hvad er dit navn? "))
f.write("^ ")
f.write(input("Hvad er dit Telefon nummer? "))
f.write("^ ")
f.write(input("Hvad er din adresse? "))
f.write("/ ")
f.close()
