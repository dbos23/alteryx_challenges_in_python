import pandas as pd

# replicate list of years
one_digit_years = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]
years = [x for x in range(1000, 9999) if x not in one_digit_years]

# create list to store the outputs from the loop
result_list = []

for year in years:
    #create count of iterations, make copies of the year so as not to overwrite the original
    count = 0
    original_year = year
    num = year
    
    while True:        
        # create a list of the numbers in the year (as strings)
        year_str = str(num)
        year_str = ('000' + year_str)[-4:] # making sure that leading zeroes are retained
        char_list = [char for char in year_str]

        # create ascending and descending lists
        chars_asc = sorted(char_list, reverse=False)
        chars_desc = sorted(char_list, reverse=True)

        # make them into numbers and identify which is smaller and which is bigger
        num_1 = int(''.join(chars_asc))
        num_2 = int(''.join(chars_desc))
        small = min(num_1, num_2)
        big = max(num_1, num_2)

        # calculate the diff and increment the iteration count
        result = big - small
        count += 1

        # determine whether to break the loop or iterate through again
        if result == 6174:
            result_list.append({'original year': original_year, 'lucky number': count})
            break
        else:
            num = result

df = pd.DataFrame(result_list)

print(df.head())