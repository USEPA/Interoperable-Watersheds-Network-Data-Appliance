class CronException(Exception):
    def __init__(self, message, data):
        super(CronException,self).__init__(message)

        self.data = data