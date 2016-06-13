# coding=utf-8

# produce a list of T-shirts available in 2 colors and 4 sizes
colors = ['black', 'white']
sizes = ['S', 'M', 'L', 'XL']

tshirts= [(color, size) for color in colors for size in sizes]


for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)