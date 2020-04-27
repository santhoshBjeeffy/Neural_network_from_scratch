'''
create a single neuron with 4 inputs 
'''

inputs=[1.1, 2.4, 3.2, 1.4]
weights=[2.1, 3.1, 1.4, 4.1]
bias1=3.0
bias2=1.5
bias3=2.1

output=[inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+inputs[3]*weights[3]+bias1,
		inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+inputs[3]*weights[3]+bias2,
		inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+inputs[3]*weights[3]+bias3]


print(output)