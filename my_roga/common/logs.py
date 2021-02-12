from home.models import LogModule, Logs

class LogAction(object):

    def __init__(self, log_module):
        self.log_module = log_module
    
    def create(self, error_type='ERROR', message=''):
        log_module = LogModule.objects.filter(name__iexact=self.log_module).first()
        if log_module:
            obj = Logs.objects.create(log_module=log_module,
                                log_type=error_type,
                                message=message)
            return obj
        return False

