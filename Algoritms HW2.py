#Split in Half
def split_in_half(s):
    lenght = len(s)
    half = lenght // 2
    add = 0

    if lenght % 2:
        add = 1

        left = s[:half + add]
        right = s[half + add:]
        print(f'left = {left}')
        print(f'right = {right}')

        print(right + left)


test_data_even = 'oooxxx'
test_data_odd = 'ooozxxx'
split_in_half(test_data_odd)
split_in_half(test_data_even)


#Unique Character in String
def unique(s):
    return len(set(s)) == len(s)


test_data_unique = '12345'
test_data_duplic = '11223344'

print(unique(test_data_unique))
print(unique(test_data_duplic))