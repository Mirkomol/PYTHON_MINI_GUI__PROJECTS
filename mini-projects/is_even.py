# Do not Like This
# numbers = [3,4,2,1,4,5,8,9,10,12]
# evens = []
# for i in numbers:
#     if i % 2 == 0:
#         evens.append(i)
#
# print(evens)

# Do Like this

def is_even(a):
    return a%2 == 0

numbers = [3,4,5,6,7,8,9,0,10,12,14,2]

evens = filter(is_even,numbers)

print(list(evens))