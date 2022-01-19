from operator import ne
from weights import backpropagation, maths_Functions, random_Weights, neuron 
from convert import conver_To_One
from file_Open import file
import random
def Image_Iteration(pixels, size):      #loaded file, size [width, height]
    width = size[0]
    height = size[1]
    list = []
    for i in range(0, width):
        for k in range(0, height):
            list.append(maths_Functions.convert(maths_Functions.sum([pixels[i,k][j] for j in range(0, 3)]), 255*3))
    return list
def open_Image(path):
    f = file(path)
    data_Of_File = f.open_Image()
    loaded_File = f.get_Colors_Of_Pixels(data_Of_File)
    size = f.get_Size(data_Of_File)
    return Image_Iteration(loaded_File, size)

class network:
    def __init__(self, topolgy): #array 
        self.topology = topolgy
        self.all_Wegiths = []
        self.this_Weight = []
    def make_Weights(self):
        self.all_Wegiths = []
        for i in range(0, len(self.topology)):
            wc = random_Weights(self.topology[i][0],self.topology[i][1])
            self.this_Weight = wc.make()
            self.all_Wegiths.append(self.this_Weight)
    def activation(self,inputs):
        self.inputs = inputs
        self.o = []
        self.s_List = []
        self.output = []
        #self.output = [maths_Functions.sig(maths_Functions.sum([self.inputs[i]*self.this_Weight[i][k] for k in range(0, len(self.this_Weight))])) for i in range(0, len(self.inputs))]
            

def main():
    #image open
    input = open_Image("images/0/0.png")
    #convert the rgb color code to number between 0-1
    topology = [[len(input), 16], [16,16], [16,10]]
    nn = network(topology)
    nn.make_Weights()
    outputs = []
    all_S = []
    nn.this_Weight = nn.all_Wegiths[0]
    nn.activation(input)
    outputs.append(nn.output)
    print(outputs)
    for i in range(1, len(nn.all_Wegiths)):
        nn.this_Weight = nn.all_Wegiths[i]
        nn.activation(outputs[len(outputs)-1])
        outputs.append(nn.output)

if __name__ == "__main__":
    main()