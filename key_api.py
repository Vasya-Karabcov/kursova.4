from abc import ABC, abstractmethod
import requests
import os


class ApiWebsite(ABC):

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(ApiWebsite, ABC):
    def get_request(self, page=0):
        params = {'page': page,
                  'per_page': 100}
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        return response

    def get_vacancies(self):
        result = self.get_request()
        pages = result.json()["pages"]
        vacancies = result.json()["items"]
        for page in range(1, pages):
            result = self.get_request(page).json()["items"]
            vacancies.extend(result)
        return vacancies


class SuperJobAPI(ApiWebsite, ABC):
    def get_request(self, page=0):
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': os.getenv('SuperJOB_API'),
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'page': page,
            'count': 20
        }
        response = requests.get('https://api.superjob.ru/3.0/vacancies/', headers=headers, params=params)
        return response.json()

    def get_vacancies(self):
        result = self.get_request()["objects"]
        vacancies = result
        for page in range(1, 25):
            res = self.get_request(page)["objects"]
            vacancies.extend(res)
        return vacancies
