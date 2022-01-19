from PIL import Image
class file:
    def __init__(self, path):
        self.path = path
    def read_File(self):
        return open(self.path)
    def write_File(self):
        pass
    def open_Image(self):
        return Image.open(self.path)
    def get_Colors_Of_Pixels(self,read_File):
        return read_File.load()
    def get_Size(self, loaded_File):
        return loaded_File.size