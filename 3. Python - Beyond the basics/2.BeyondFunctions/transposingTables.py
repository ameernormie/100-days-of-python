from pprint import pprint as pp

sunday = [1, 2, 3, 4, 5, 6, 7, 8]
monday = [9, 10, 11, 12, 13, 14, 15, 16]
tuesday = [17, 18, 19, 20, 21, 22, 23, 24]


daily = [sunday, monday, tuesday]


for item in zip(*daily):
    print(item)

# pp(daily)
transposed = list(zip(*daily))
pp(transposed)
