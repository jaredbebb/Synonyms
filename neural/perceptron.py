class perceptron:
    def __init__(self, _weight, _inputs):
        self.inputs = _inputs
        self.weight = _weight
        self.weighted_inputs = []
        self.sum_inputs = 0

    def weight_inputs(self):
        for curr in self.inputs:
            weighted_input = (curr*(self.weight/len(self.inputs)))
            self.weighted_inputs.append(weighted_input)
        bias = 1
        self.weighted_inputs.append(bias)
        
    def recieve_inputs(self):
        sum = 0
        for i in self.weighted_inputs:
            sum+=i
        return sum

    def tranformation(self, threshhold):
        received_inputs = self.recieve_inputs()
        if received_inputs > threshhold:
            return 1
        else:
            return 0

    def check_results(self):
        return True

_inputs = [4,4,4,4]
percept = perceptron(1, _inputs)
percept.weight_inputs()
print(percept.tranformation(4))


