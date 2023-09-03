from key_api import HeadHunterAPI, SuperJobAPI
from jsonsaver import JSONSaver
from vacancy import VacancyHH, VacancySuperJob
from functions import get_filtering

platform = int(input('Введите номер платформы для поиска(1 - HeadHunter, 2 - SuperJob): '))
if platform == 1:
    # объект для работы с API HeadHunter
    plat_hh = HeadHunterAPI()

    # получить список всех вакансий(ограничение 2 000 вакансий)
    vacancies = plat_hh.get_vacancies()

    # подготовка списка вакансий к записи в файл.json
    hh_vacancy = VacancyHH(vacancies)
    vacancies = hh_vacancy.get_list_vacancies()

elif platform == 2:
    # объект для работы с API SuperJob
    plat_sj = SuperJobAPI()
    # получить список всех вакансий(ограничение 500 вакансий)
    vacancies = plat_sj.get_vacancies()
    # подготовка списка вакансий к записи в файл.json
    plat_sj_vacancy = VacancySuperJob(vacancies)
    vacancies = plat_sj_vacancy.get_list_vacancies()
else:
    quit('Выбранной платформы не существует')

# объект класса JSONSaver
json_saver = JSONSaver(vacancies)

# сохранение списка вакансий в json
json_saver.save_to_json()

search_word, sorting, count_top = get_filtering()
if sorting == 2:
    # фильтр вакансий по поисковому запросу
    print(json_saver.filter_vacancies(search_word))
else:
    # фильтр вакансий по поисковому запросу
    filter_vacancies = json_saver.filter_vacancies(search_word)
    # вывод отсортированного списка вакансий по зарплате
    sorting_vacancies = json_saver.get_vacancies_by_salary(filter_vacancies)
    print(f'Найдено {len(sorting_vacancies)} вакансий.')

    # вывод топ-вак.
    if int(count_top) > len(sorting_vacancies):
        count_top = len(sorting_vacancies)
    print(f'Топ-{count_top} вакансий')
    top_vacancies = json_saver.get_top_vacancies(count_top, sorting_vacancies)
    print(*top_vacancies, sep='\n')
