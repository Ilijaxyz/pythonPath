print("Hello binary gap")


def convert_binary(num):
  bin_list = []
  res = num
  while res != 0: 
    res = res // 2
    bin_list.append(res % 2)
  return bin_list[::-1]

def find_longest(num):
  bin_list = convert_binary(num)
  count = 0
  maxes = []
  first_one = bin_list.index(1)
  for i in range(first_one + 1,len(bin_list)):
    if bin_list[i] != 1:
      count += 1
    elif bin_list[i] == 1 and count > 0:
      maxes.append(count)
      count = 0
  if len(maxes) > 0:
    return max(maxes)
  return 0
    
print(find_longest(1041))