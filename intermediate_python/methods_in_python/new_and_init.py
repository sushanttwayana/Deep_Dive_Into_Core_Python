from multiprocessing import connection


class Connection:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        
        if cls._instance is None:
            print("Connecting.....")   
            cls._instance = super().__new__(cls) 
        
            return cls._instance

        else:
            print("Warning: There\'s already an instance of connection!")

            return cls._instance

    
    def __init__(self) -> None:
        print("Connected to internet!!")


connection1 = Connection()
connection2 = Connection()

print(connection1 == connection2)