#answer times first num
def multiply(first_num, second_num):
    answer = 0
    for times in range(second_num):
        answer += first_num
    return answer
        
print("Answer = ", multiply(3,2))

def power(first_num, second_num):
    if second_num == 0:
        return 1
    else:
        answer = 1
        for called_times in range(second_num ):
            answer = multiply(answer,first_num)
        return answer
print("Answer = ", power(3, 3))

def divide(first_num, second_num):
    result = first_num
    counter = 0 
    remainder = 0
    while result > 0:
        result = result - second_num
        counter += 1
    if result < 0:
        remainder = result + second_num
    return str(str(first_num) + "/" + str(second_num) + "=" + str(result) + " with " + str(remainder) + " remainder(s)")
    

divide(6,2)