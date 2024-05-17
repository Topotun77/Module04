def hello_w():
    print('Привет, Мир!')


def hello_w2(*h_w):
    if h_w == ():
        h_w = ('Привет, Мир!',)
    print(*h_w)


print(__name__)
if __name__ == '__main__':
    hello_w()
    h_w = 'Привет, Мир!'
    hello_w2(h_w)
    hello_w2()
    hello_w2(678, 'Qwerty')
