import pandas as pd
import math
import sys

input_num = 100
diff = 1

while True:
    # each of these candidates gets increasingly far from input_num each time the loop runs
    cand_1 = input_num + diff
    cand_2 = input_num - diff

    # the number of divisors each candidate has (not including 1 and itself)
    count_1 = 0
    count_2 = 0

    # each number that could be a divisor is checked to see if it is
    for divisor in range(2, math.ceil((cand_1 / 2) + 1)):
        if (round(cand_1 / divisor) == cand_1 / divisor):
            count_1 += 1

        if (round(cand_2 / divisor) == cand_2 / divisor):
            count_2 += 1

    # numbers with no divisors are prime so the script can report on them and terminate
    if count_1 == 0:
        print(f'Closest prime: {cand_1}')
        sys.exit()
    elif count_2 == 0:
        print(f'Closest prime: {cand_2}')
        sys.exit()

    diff += 1