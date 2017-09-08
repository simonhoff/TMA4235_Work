import numpy as np
import matplotlib as plot

N = 1000000

num_fakes = 0
num_heads = 0

for i in range(N):
    prob = np.random.uniform()
    if prob > 0.5: # fake coin
        num_fakes += 1
        num_heads += 1
    else: # Non-fake coin
        prob = np.random.uniform()
        if prob > 0.5:
            num_heads += 1
        # else not valid

print("Probability of fake coin given head, with N="+str(N))
print("is "+str(num_fakes/num_heads))


num_heads = 0
num_fakes = 0
NUM_TOSSES = 3


for i in range(N):
    prob = np.random.uniform()
    if prob > 0.5: # fake coin
        num_fakes += 1
        num_heads += 1
    else: # Non-fake coin
        prob = np.random.uniform()
        toss_no = 0
        while prob > 0.5 and toss_no < NUM_TOSSES:
            prob = np.random.uniform()
            toss_no += 1
        if toss_no == NUM_TOSSES:
            num_heads += 1
        # else not valid

print("Probability of fake coin given head, with N="+str(N)+",")
print(" and " +str(NUM_TOSSES)+ " tosses is "+str(num_fakes/num_heads))

