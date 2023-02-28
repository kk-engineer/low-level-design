
from threading import Lock, Thread
from colorama import Fore
import threading


class SingletonMeta(type):
    _instance = None
    _lock: Lock = Lock()
    _count = 0

    def __call__(cls, *args, **kwargs):
        # Double check locking
        if not cls._instance:
            # Acquire lock
            with cls._lock:
                #cls._count+=1
                print(Fore.CYAN + "\nAcquired lock : Entering critical section \n")
                # Check if instance already created before creating an instance
                if not cls._instance:
                    print("Create a new instance !")
                    instance = super().__call__(*args, **kwargs)
                    cls._instance = instance
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print("\n")
    print(threading.current_thread().name)
    print(singleton.value)
    print("\n")


if __name__ == "__main__":

    #from logging_service import LoggingService

    #log = LoggingService()
 
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
    process3 = Thread(target=test_singleton, args=("KK",))
    process4 = Thread(target=test_singleton, args=("AK",))
    process5 = Thread(target=test_singleton, args=("Y2K",))
    process3.start()
    process4.start()
    process5.start()

    """ s1 = Singleton("KK")
    print(s1.value) """

    