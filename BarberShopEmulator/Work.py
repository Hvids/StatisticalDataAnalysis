import pandas as pd
from Event import Events


class Worker:
    def __init__(self, barber_shop):
        self.barber_shop = barber_shop

    # Начало работы экперимента
    def work(self):
        self.events = Events.make_start_events(self.barber_shop)
        self.events.start(self.barber_shop)

    @property
    def report(self):
        return self.events.report

