meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "CYA": "Puede significar una despedida",
            "BTW": "Significa porcierto, de forma corta",
            "GTG": "Me tengo que ir, de forma corta"
            }
for i in range(5):
    
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("Esta palabra significa esto:",meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Esta palabra no esta disponible.")
