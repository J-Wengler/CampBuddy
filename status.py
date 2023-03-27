class Status:
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def get_status(self):
        return self.status
    
    def get_message(self):
        return self.message