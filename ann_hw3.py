try:
    training_data = open('training_data_2n.txt', 'r')

except:
    print "Can't find training data for two-neuron ADALINE network. Please make sure training_data_2n.txt is under the same directory as this py file."
    quit()

data = training_data.readlines()
weight = [1.0, 0.0, 0.0, 1.0]
bias = [1.0, 1.0]
learning_rate = 0.1

for i in range(0, len(data), 4):
    for j in 