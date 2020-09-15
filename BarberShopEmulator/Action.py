import pandas as pd
class Action:
    def __init__(self,time,hairdressers, queue_clients):
        self.time = time
        self.status_hairdressers = [hairdresser.report_status for hairdresser in hairdressers]
        self.size_queue = len(queue_clients)
    def __str__(self):
        return f'{self.time} | {self.status_hairdressers} | {self.size_queue}'
    @property
    def report_row(self):
        return [self.time] + self.status_hairdressers + [self.size_queue]
class Actions:
    def __init__(self, actions=[]):
        self.actions = actions

    def add_action(self, action):
        self.actions.append(action)

    def delete_action(self,action):
        self.actions.remove(action)

    @property
    def report(self):
        columns_report = ['time'] + [f'hairdresser {i+1}' for i in range(len(self.actions[0].status_hairdressers)) ] + ['queue']
        report = pd.DataFrame(columns=columns_report)
        for action in self.actions:
            report.loc[report.shape[0]] = action.report_row
        return report