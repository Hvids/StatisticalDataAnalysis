import random
import numpy as np

FREE = 'FREE'
WORK = 'WORK'


class Hairdressers:
    def __init__(self):
        self.hairdressers = []

    def __iter__(self):
        for hairdresser in self.hairdressers:
            yield hairdresser

    #Вернуть всех свободных парикхмахеров
    @property
    def free_hairdressers(self):
        free_hairdresser = [hairdresser for hairdresser in self.hairdressers if hairdresser.is_free == True]
        return free_hairdresser

    #Выбрать свободного парикхмажера из спика свободных
    @staticmethod
    def select_hairdresser(free_hairdresser):
        size = len(free_hairdresser)
        idx = np.random.choice(size, 1)[0]
        return free_hairdresser[idx]

    #Добавить парикхмахера
    def add(self, hairdresser):
        self.hairdressers.append(hairdresser)

    #Удалить парикхмахера
    def delete(self, hairdresser):
        self.hairdressers.remove(hairdresser)


class Hairdresser:
    def __init__(self, mean_time_work, min_time_work=10):
        self.mean_time_work = mean_time_work
        self.alpha = 1 / mean_time_work
        self.mean_time_work = mean_time_work
        self.status = FREE

    #Вернуть время работы над клиентом
    @property
    def time_work(self):
        time = random.expovariate(self.alpha)
        while time < self.mean_time_work:
            time = random.expovariate(self.alpha)
        return time

    #Свободен ли парикхмахер
    @property
    def is_free(self):
        return self.status == FREE
    #Занят ли парикхмахер
    @property
    def is_work(self):
        return self.status == WORK

    #Сделать его занятым
    def make_work(self):
        self.status = WORK
    #Сделать свободным
    def make_free(self):
        self.status = FREE

    @property
    def report_status(self):
        if self.is_free:
            return 'Свободен'
        else:
            return 'Занят'