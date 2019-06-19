

#PF-Assgn-57


def check_prime(number):
    i = 2
    if(number==2):
        return True
    while(i<number):
        if(number%i==0):
            return False
        i+=1
    return True

def rotations(num):
    
    num_str = str(num)
    count = 0
    rotated_list = []
    x = 0
    while(count<len(num_str)):
        one = (num_str[:x])
        two = num_str[x:]
        count+=1
        x+=1
        rotated_list.append(int(str(two)+str(one)))
    return rotated_list
        




def get_circular_prime_count(limit):
    count = 0
    for num in range(2, limit):
        rotation_list = rotations(num)
        flag = 0
        for rotation in rotation_list:
            if(check_prime(rotation)):
                continue
            else:
                flag = 1
                break
        if(flag==0):
            count+=1

    return count


print(get_circular_prime_count(1000))