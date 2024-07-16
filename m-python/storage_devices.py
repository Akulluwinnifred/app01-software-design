from abc import ABC, abstractmethod



class StorageDevice(ABC):
    @abstractmethod
    def store_data(self) -> str:
        pass
    
    @abstractmethod
    def retrieve_data(self) -> str:
        pass



class SSD(StorageDevice):
    def store_data(self):
        return "Storing data to SSD..."
    
    def retrieve_data(self):
        return "Retrieving data from SSD..."


class HDD(StorageDevice):
    def store_data(self):
        return "Storing data to HDD..."
    
    def retrieve_data(self):
        return "Retrieving data from HDD..."