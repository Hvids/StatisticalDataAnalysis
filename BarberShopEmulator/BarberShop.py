from scipy.stats import poisson
from Hairdresser import Hairdresser, Hairdressers
from QueueClient import QueueClients
from Event import EventCloseVisit
from Action import  Action
from Time import Time
import random


class BarberShop:
    def __init__(self,  mean_time_wait_client, time_period,start_time_work=Time(10,0)):
        self.start_time_work = start_time_work
        self.mean_time_wait_client = mean_time_wait_client
        self.time_period = time_period
        self.alpha = 1 / mean_time_wait_client
        self.count_clients = self.__count_clients
        self.hairdressers = Hairdressers()
        self.queue_clients = QueueClients()

    #Закрыть визит клиента
    def close_visit(self, time, hairdresser):

        hairdresser.make_free()
        if len(self.queue_clients) > 0:
            self.queue_clients.pop()
            hairdresser.make_work()
            time_work = hairdresser.time_work
            event = EventCloseVisit(time + time_work, hairdresser)
        else:
            event = None
        action = Action(self.start_time_work + time, self.hairdressers, self.queue_clients)
        return action, event

    #Добавить клиента в очередь или к парикхмахеру
    def add_client(self, time, client):
        free_hairdresser = self.hairdressers.free_hairdressers
        if len(free_hairdresser) == 0:
            self.queue_clients.add(client)
            event = None
        else:
            hairdresser = self.hairdressers.select_hairdresser(free_hairdresser)
            hairdresser.make_work()
            time_work = hairdresser.time_work
            event = EventCloseVisit(time + time_work, hairdresser)
        action = Action(self.start_time_work + time, self.hairdressers, self.queue_clients)
        return  action, event

    #Время ожидание следующего клиента
    @property
    def time_wait_client(self):
        time = random.expovariate(self.alpha)
        return round(time)

    #Сделать пустой отчет работы
    def make_result_empty(self, result):
        for i, hairdresser in enumerate(self.hairdressers):
            result[f'{hairdresser} {i + 1}'] = []
        return result

    #Добавить Парикхмахера
    def add_hairdresser(self, hairdresser):
        self.hairdressers.add(hairdresser)

    #Удалить парикхмахера
    def delete_hairdresser(self, hairdresser):
        self.hairdressers.delete(hairdresser)

    @property
    def __count_clients(self):
        return poisson.rvs(self.time_period * self.alpha, size=1)[0]



