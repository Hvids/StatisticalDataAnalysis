class QueueClients:
    def __init__(self):
        self.cients = []

    #Добавить клиента
    def add(self, client):
        self.cients.append(client)

    #Удалить клиента в возращением
    def pop(self):
        return self.cients.pop(0)

    def __len__(self):
        return len(self.cients)