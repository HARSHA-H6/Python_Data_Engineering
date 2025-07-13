import random

def flip_coin():
    return random.choice(['Head','Tail'])

def run_flip_coin(times):
    if not isinstance(times,int) or times<0:
        return f"Please enter the non-negative interger as the input"
    
    heads_count = 0
    for _ in range(times):
        if flip_coin()=='Head':
            heads_count+=1
    
    if times ==0:
        percentage_heads = 0.0
    else:
        percentage_heads = (heads_count/times)*100
    
    return f"After flipping the coin {times} times, The percentage of times head has come is: {percentage_heads:.2f}%"


times_entered= (input("Enter the number of times the coin should be flipped: "))
times = times_entered.isdigit() and int(times_entered) or None
print(run_flip_coin(times))