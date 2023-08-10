from abc import ABC, abstractmethod
class Image(ABC):
    @abstractmethod
    def load_image(self, filename):
        pass
    
    @abstractmethod
    def save_image(self, filename):
        pass

class Bitmap(Image):
    def load_image(self, filename):
        print(f"Loading Bitmap image from {filename}")
    def save_image(self, filename):
        print(f"Saving Bitmap image to {filename}")

class Jpeg(Image):
    def load_image(self, filename):
        print(f"Loading JPEG image from {filename}")
    def save_image(self, filename):
        print(f"Saving JPEG image to {filename}")

if __name__ == '__main__':
    bitmap1 = Bitmap()
    bitmap1.save_image('kku.bmp')
    bitmap1.load_image('kku.bmp')
    jpeg1 = Jpeg()
    jpeg1.save_image('en.jpg')
    jpeg1.load_image('en.jpg')