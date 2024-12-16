import inpoput
import maclaurin
import menu


def main():
    """Начал головной функции main"""
    x = inpoput.inpp()
    while True:
        menu.menu()
        try:
            inp = int(input('Введите номер команды,'
                            'которую хотите реализовать '))
            if inp > 5 or inp < 1:
                print("введен не коректный номер")
                continue
            match inp:
                case 1:
                    maclaurin.ch_maclaurin(x)
                case 2:
                    maclaurin.ln_one_minus_x_maclaurin(x)
                case 3:
                    maclaurin.arctan_maclaurin(x)
                case 4:
                    x = inpoput.inpp()
                case 5:
                    break
        except ValueError:
            print('Введены некорректные данные')
        continue


if __name__ == '__main__':
    main()
