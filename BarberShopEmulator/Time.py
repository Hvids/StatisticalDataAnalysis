class Time:
    def __init__(self,hour=0,minute = 0):
        self.hour = hour
        self.minute = minute

    def __add__(self, other):
        minute = other + self.minute
        hour = (self.hour + minute//60)%24
        minute = round(minute) % 60
        minute = round(minute)
        hour = int(hour)
        return Time(hour, minute)

    def __iadd__(self, other):
        minute = other + self.minute
        self.hour =  (self.hour + minute // 60)%24
        self.hour = int(self.hour)
        self.minute = round(minute)%60
        return self

    def __str__(self):
        hour = f'{self.hour}' if self.hour >= 10 else f'0{self.hour}'
        minute = f'{self.minute}' if self.minute >= 10 else f'0{self.minute}'
        return f'{hour}:{minute}'

