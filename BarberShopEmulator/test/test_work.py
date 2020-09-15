import sys

sys.path.append('../')
from BarberShop import BarberShop
from Hairdresser import Hairdresser
from Work import Worker

mean_time_wait_client = 5
time_period = 30
time_works = [29, 30, 15]

barber = BarberShop(mean_time_wait_client, time_period)
for time_work in time_works:
    barber.add_hairdresser(Hairdresser(time_work))

worker = Worker(barber)
worker.work()
print(worker.report)