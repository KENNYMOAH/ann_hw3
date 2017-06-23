try:
    training_data = open('training_data.txt', 'r')

except:
    print "Can't find training data. Please make sure training_data.txt is under the same directory as this py file."
    quit()

data = training_data.readlines()
weight = [1.0, 0.0, 0.0, 1.0]
bias = [1.0, 1.0]
learning_rate = 0.1
a = [0.0, 0.0]
e = [0.0, 0.0]
output = [0.0, 0.0, 0.0, 0.0]

for i in range(0, len(data), 4):
    for j in range(0, 2):
        a[j] = float(weight[2 * j]) * float(data[i]) + float(weight[2 * j + 1]) * float(data[i + 1]) + bias[j]
        e[j] = float(data[i + j]) - a[j]
    
    for j in range(0, 2):
        for k in range(0, 2):
            weight[2 * j + k] += learning_rate * float(e[j]) * float(data[i + k])
        bias[j] += learning_rate * e[j]
    
    # print "Weight " + str(i / 4 + 1) + ":\n" + str(weight[0]) + "\t" + str(weight[1]) + "\n" + str(weight[2]) + "\t" + str(weight[3])
    # print "Bias " + str(i / 4 + 1) + ": [" + str(bias[0]) + " " + str(bias[1]) + "]"

print "Learning complete successfully."
training_data.close()

try:
    testing_data = open('testing_data.txt', 'r')

except:
    print "Can't find testing data. Please make sure testing_data.txt is under the same directory as this py file."
    quit()

