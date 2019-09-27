import json

name_file = 'postavy'
file_path = f'{name_file}.json'
#intro
print('Vitej, cizince. Nevim jak se ti to podarilo, ale bohuzel jsi se nejak dostal k teto hre a ted ti nezbyva nic jineho, nez si ji zahrat')
print('Hra je jednoducha. Dnes jsi se rozhodl vyrazit do klubu za jedinym cilem. Zaschwazat si. Hrou te budu doprovazet ja.')
#Funkce na zadani vlastního jména
while True:
    nick = input('Zacneme tim, ze mi reknes sve jmeno: ')
    print(f'Jsi spokojeny se svym jmenem, {nick}?\n')
    break
'''
    text = 'Zadej "a" pokud jsi spokojen a "n" pokud nejsi spokojen: '
    odpoved = input(text).lower()
    def zadani_jmena():
        if odpoved == 'a':
            print('Jsi sikula!')
        elif odpoved == 'n':
            print('Nic se nedeje, jmeno si muzes zmenit.')
            break
        else:
            print('Musis zadat bud "a" jakozto souhlas spokojenosti a nebo "n" jakozto nesouhlas.')
'''   
#Zadani veku
while True:
    vek = input('Ted mi prosim zadej svuj vek: ')
    if vek.isdigit():
        vek = int(vek)
        if 0<= vek < 15 or vek >= 100:
            print('Promin, ale pro vstup ti musi byt vice nez 15 let a mene nez 100')
        else:
            print('Naprosto v poradku')
            break
    else:
        print('Musis zadat spravne cislo')


#Vypise ti postavy, ktere dnes budes moci opichat ovsem bez jejich jmen, ktere zjistis az v prubehu hry.
print('Ted ti predstavim postavy, ktere dneska muzes nabalit. Zatim neznas jejich jmena, jelikoz je ( snad, hehe ) zjistis v prubehu hry.\nOvsem vybrat si muzes az za chvilku.')
with open(file_path, 'r') as file_handler:
    json_postavy = json.load(file_handler)

for item in json_postavy:

    vek = json_postavy[item]['vek']
    pohlavi = json_postavy[item]['pohlavi']
    opilost = json_postavy[item]['opilost']
    vzhled = json_postavy[item]['vzhled']
    inteligence = json_postavy[item]['inteligence']
    jmeno = json_postavy[item]['jmeno']
    obtiznost = json_postavy[item]['obtiznost']

    print(f'Postava cislo: {item}')
    print(f'    Pohlavi: {pohlavi}')
    print(f'    opilost: {opilost}')
    print(f'    vzhled: {inteligence}\n')


#Zadani tve orientace
while True:
    print('Posledni otazka kterou na tebe mam je, zda-li hledas zenu ci muze. ')
    orientace = input('Pokud jsi na kluky zadej "1". Pokud jsi na holky, zadej "2": ')
    if orientace.isdigit():
        orientace = int(orientace)
        if orientace == 1:
            print('Dneska si tedy dotahnes domu muze.')
            break
        elif orientace == 2:
            print('Dneska si tedy dotahnes domu zenu.')
            break
        else:
            print('Musis zadat bud "1" nebo "2"')
    else:
        print('Musis zadat cislo. ')

print('Dobra. Zopakujeme si informace o tobe.')
print(f'Jmenujes se {nick},')
print(f'Je ti {vek} let,')
if orientace == 1:
    print('A jsi na kluky.')
else:
    print('A jsi na holky.')




