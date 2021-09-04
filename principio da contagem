# https://acaciomk.com.br/
s = input('informe se os evento serão simultâneos S/N: ')
s = s.upper()
if s == 'S' or s == 'N':
    if s == 'S':
        simul = True
    else:
        simul = False

    event1 = input('informe o número de elemento no primeiro evento: ')
    if event1.isnumeric() == True:
        event2 = input('informe o número de elemento no segundo evento: ')
        if event2.isnumeric() == True:

            if simul == True:
                rs = int(event1) * int(event2)

                print('O evento 1 com {0} elementos e o evento 2 com {1} elementos tem {2} possibilidades de resultado'
                      .format(event1, event2, rs))
            else:
                rs = int(event1) + int(event2)

                print('O evento 1 com {0} elementos e o evento 2 com {1} elementos tem {2} possibilidades de resultado'
                      .format(event1, event2, rs))

else:
    print('não reconhecemos essa entrada')
