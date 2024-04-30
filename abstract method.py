class Product(ABC):
    @abstractmethod
    def getImageURL(self):
        pass
 
    @abstractmethod
    def getRatings(self):
        pass
 
    @abstractmethod
    def getReviews(self):
        pass
 
class Car(ABC):
    @abstractmethod
    def getCarBrand(self):
        pass 
 
    @abstractmethod
    def getPrice(self):
        pass
 
    @abstractmethod
    def getColour(self):
        pass
 
    def getNumberOfWheels(self):
        return 4 
 
