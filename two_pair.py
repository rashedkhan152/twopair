
def get_aspected_index(two_pair_values, target_value):
 

    for i in range(len(two_pair_values) - 1):
        for j in range(i + 1, len(two_pair_values)):
 
            if two_pair_values[i] + two_pair_values[j] == target_value:
                print('Pair found', (two_pair_values[i], two_pair_values[j]))
                return
 
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    two_pair_values = [
       [1, 5],
       [9, -7],
       [0, 8],
       [6, 3],
       [4, 11],
       [14, 0],
       [8, 1],
       [4, 9],
    ]
target_value = 9
 
result = get_aspected_index(two_pair_values, target_value)
print(result)