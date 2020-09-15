import json

from BarberShop import BarberShop
from Hairdresser import Hairdresser
from Work import Worker

path_file = './'
name_file = 'input_data.json'

with open(path_file + name_file) as f:
    input_data = json.load(f)

mean_time_wait_client = input_data['mean_time_wait']
time_work_barber_shop_period = input_data['time_work_barber_shop_period']
time_work_hairdressers = input_data['time_work_hairdressers']

barber = BarberShop(mean_time_wait_client, time_work_barber_shop_period)
for time_work in time_work_hairdressers:
    barber.add_hairdresser(Hairdresser(time_work))

worker = Worker(barber)
worker.work()
worker.report.to_html('./report.html')