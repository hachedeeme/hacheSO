
class Log():
    ## Singleton Magic
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Log, cls).__new__(cls, *args, **kwargs)
        return cls._instance