dict = {
    "Alvin": ["Innova", "M2", "GLS600", "Palisade"],
    "Aaron": ["CRV", "Ertiga", "G63"],
    "Michelle": ["Avanza", "Gran Max", "Terios"],
    "Angela": ["Accord", "Fortuner", "Pajero"],
    "Felix": ["Camry", "Captiva", "Camaro"]
}

for key in dict.keys():
    print(key, "likes these cars:")
    for element in list(dict.get(key)):
        print("-", element)
    print()  # to make it neater