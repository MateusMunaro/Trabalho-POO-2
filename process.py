class Process:
    def __init__(self, pid: int) -> None:
        self.__pid = pid
        
    @property
    def pid(self):
        return self.__pid
    
    @pid.setter
    def pid(self, pid: int):
        self.__pid = pid  
        
    def execute(self) -> None:
        pass
        
    def __dict__(self):
        return {
            "pid": self.pid,
            "type": self.__class__.__name__
        }
