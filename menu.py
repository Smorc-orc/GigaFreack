def menu():
    """Меню бленб"""
    lst1 = ['Поиск ch x(гиперболического косинуса)',
            'Поиск натурального логарифма ln(1-x) в пределах (−1,1].',
            'Поиск arctg x в пределах [−1,1].', 'Изменить входные парамметры',
            'Выйти']
    lst2 = [1, 2, 3, 4, 5]
    for i in range(len(lst1)):
        print(f'{lst2[i]} - {lst1[i]}')