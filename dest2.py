mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
AKT_ROK = 2021
print("VITEJTE U NASI APLIKACE DESTINATIO!\n",dvojita_cara,nabidka,dvojita_cara)
destinace = input("VYBER CISLO DESTINACE: ")
if int(destinace)>6 or int(destinace)<1:
    print (f"VYBER:{int(destinace)} NEEXISTUJE! UKONCUJI..")
    quit()
else:
    upravena_destinace = mesta[int(destinace)-1]
print("DESTINACE: ", upravena_destinace)
print(cara)
if upravena_destinace  in slevy:
    nova_cena = 0.75*ceny[int(destinace) - 1]
    print(f"ZISKAVATE 25% SLEVU! CENA: {nova_cena}")
    print(cara)
else:
    nova_cena = ceny[int(destinace) - 1]
    print("Cena: ", nova_cena)
jmeno = input("Jmeno: ")
prijmeni = input("Prijmeni: ")
print(cara)
if jmeno.isalpha() and prijmeni.isalpha():
    print(f"Cele jmeno: {jmeno} {prijmeni}")
else:
    print("Jmeno nebo prijmeni nejsou v poradku! Ukoncuji..")
    quit()
print(cara)
email = input("Email: ")
if email.find("@") and email.split("@")[1] in domeny:
    print("Email je v poradku\n",dvojita_cara)
else:
    print("Neplatna emailova adresa. Ukoncuji..")
    quit()
print(f"""DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {upravena_destinace}, CENA JIZDNEHO: {nova_cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")

