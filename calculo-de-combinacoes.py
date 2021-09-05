# https://acaciomk.com.br/
times = int(input('informe a quantidade de times que disputarão o campeonato: '))
timesSimul = 2
def fatorial(n):
    count = int(n)
    result = 1
    while (count >= 2):
        result *= count
        count -= 1

    return result

print('temos a seguinte equação: ')
print('                 {0}!'.format(times))
print('C({0}, {1}) = -------------'.format(times, timesSimul))
print('           2! ({0} - {1})!'.format(times, timesSimul))

print('E temos o seguinte resultado: ')


f1 = fatorial(times)

f2 = fatorial(timesSimul)

f3 = times - timesSimul

f3 = fatorial(f3)

rs = f1 / (f2 * f3)

rs = int(rs)

print('Teremos um total de {} jogos'.format(rs))
