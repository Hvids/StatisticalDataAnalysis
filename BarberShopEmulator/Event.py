from Client import Client
from Action import Actions, Action

class Event:
    def __init__(self, time):
        self.time = time
        self.name = 'event simple'

    #Начать совершение события
    def make(self, barber_shop):
        pass

    def __str__(self):
        return self.name

class EventCloseVisit(Event):
    def __init__(self, time, hairdresser):
        self.time = time
        self.hairdresser = hairdresser
        self.name = 'EventCloseVisit'

    def make(self, barber_shop):
        action, event = barber_shop.close_visit(self.time, self.hairdresser)
        return action, event


class EventVisitClient(Event):

    def __init__(self, time, client):
        self.time = time
        self.client = client
        self.name = 'EventVisitClient'

    def make(self, barber_shop):
        action, event = barber_shop.add_client(self.time, self.client)
        return action, event


class Events:
    def __init__(self, events=[], actions = Actions()):
        self.events = sorted(events, key=lambda v: v.time)
        self.actions = actions
        #Начать происхождение событий
    def start(self, barber_shop):

        while len(self.events) > 0:
            event = self.get_event_with_remove()
            action, event = event.make(barber_shop)
            self.actions.add_action(action)
            self.add(event)


    @property
    def report(self):
        return self.actions.report
    #Получить событие на очереди
    def get_event_with_remove(self):
        return self.events.pop(0)

    #Создать начальные события
    @classmethod
    def make_start_events(cls, barber_shop):
        time = 0
        events = []
        for _ in range(barber_shop.count_clients):
            time_wait = barber_shop.time_wait_client
            time += time_wait
            events.append(EventVisitClient(time, Client()))
        action = Action(
            time=barber_shop.start_time_work,
            hairdressers=barber_shop.hairdressers,
            queue_clients=barber_shop.queue_clients)
        return cls(events=events, actions=Actions([action]))

    #Добавить событие
    def add(self, event):
        if not event == None:
            self.events.append(event)
            self.events = sorted(self.events, key=lambda v: v.time)
