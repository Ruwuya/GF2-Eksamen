try:
    f = open("Database.txt", "r")
    Database = f.read()
    Search = input("Skriv et Navn du søger efter: ")
    Anton = Database.index(Search)
    Slash = Database.index("/", Anton)
    print(Database[Anton:Slash].split("^ "))
    

except Exception:
    print("Fejl i txt fil")
    quit()

