

import math

x = -87780
new_x = abs(x)
list = [int(x) for x in str(new_x)]
reverse_list = list[::-1]
result = []
time = 1




# if x < - pow(2,31) or x > pow(2,31) - 1:
#     return None
# elif:
for n in reverse_list:
    if n == 0 and time == 1:
        time += 1
    else:
        result.append(n)
        time += 1

strings = [str(result) for result in result]
a_string = ''.join(strings)


an_int = int(a_string)

if x >= 0:
    print(an_int)
else:
    print(0 - an_int)










