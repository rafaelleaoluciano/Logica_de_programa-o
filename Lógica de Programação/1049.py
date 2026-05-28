filo = input()
classe = input()
heterótrofo = input()

if filo == 'vertebrado':
    if classe == 'ave':
        if heterótrofo == 'carnivoro':
            print('aguia')
        elif heterótrofo == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if heterótrofo == 'onivoro':
            print('homem')
        elif heterótrofo == 'herbivoro':
            print('vaca')
elif filo == 'invertebrado':
    if classe == 'inseto':
        if heterótrofo == 'hematofago':
            print('pulga')
        elif heterótrofo == 'herbivoro':
            print('lagarta')
    elif classe == 'anelideo':
        if heterótrofo == 'hematofago':
            print('sanguessuga')
        elif heterótrofo == 'onivoro':
            print('minhoca')


