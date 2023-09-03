def get_filtering():
    """
    Работа с пользователем
    """
    search_word = input('Введите поисковый запрос:')

    sorted_list = 0
    while int(sorted_list) not in (1, 2):
        sorted_list = input('Отсортировать список по зарплате? Введите:("1" если ДА, "2" если НЕТ)')
        if sorted_list.isdigit():
            if int(sorted_list) not in (1, 2):
                print('Введено некорректное значение\nПовторите попытку')
        else:
            sorted_list = 0
            print('Введено некорректное значение\nПовторите попытку')

    while True:
        count_top_vacancies = input('Введите количество топ-вакансий для вывода (только целое число)')
        if count_top_vacancies.isdigit():
            return search_word, sorted_list, count_top_vacancies
        else:
            print('Введено некорректное значение\nПовторите попытку')
