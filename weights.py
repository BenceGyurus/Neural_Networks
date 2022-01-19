import math
import random
class maths_Functions:
    def sig(x):
        return 1/(1+math.e**(-1*x)) 
    def sig_Derival(x):
        return maths_Functions.sig(x)*(1-maths_Functions.sig(x))
    def sum(array):
        x = 0
        for i in array:
            x += i
        return x
    def avtivation_Function(input, weight):
        return input*weight
    def convert(x, max):
        return x/max


class random_Weights:
    def __init__(self, x, y):
        self.neuron_X = x
        self.neuron_Y = y
    def make(self):
        return [[random.randint(0,9999)/10000 for _ in range(0, self.neuron_Y)] for i in range(0, self.neuron_X)]
    def make_Bias(self):
        return [random.randint(0,10)/10 for _ in range(0, self.neuron_X)]
class neuron:
    def __init__(self,weight,inputs,x,y, biases):
        self.weights = weight
        self.neuron_X = x
        self.neuron_Y = y
        self.inputs = inputs
        self.bias = biases
    def calc(self):
        r = []
        for i in range(0, self.neuron_X):
            x = []
            for k in range(0, self.neuron_Y):
                x.append(maths_Functions.avtivation_Function(self.inputs[i],self.weights[i][k]))
            else:
                x.append(self.bias[i])
                a = maths_Functions.sum(x)
                print(a)
                r.append(maths_Functions.sig(a))
        return r

class backpropagation:
    def __init__(self, inputs,output ,w, bias, target):
        self.inputs = inputs
        self.w = w
        self.bias = bias
        self.output = output
        self.target = target
        self.learning_Rate = 0.1
    def calc_Output_Delta_W(self):
        for i in range(0, len(self.output)):
            for k in range(0, len(self.w[len(self.w)-1][i])):
                delta_K = (self.target[i]-self.output[i])*self.output[i]*(1-self.output[i])
                self.w[len(self.w)-1][i][k] = self.learning_Rate*delta_K*self.output[i]
        return self.w
    def calc_Hidden_W(self):
        pass