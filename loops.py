item = []
price = []
quantity = []

while True:
        item.append(raw_input('item (enter "done" when finished): '))
        if item[-1].lower() == "done":
                break
        price.append(float(raw_input('price: ')))
        quantity.append(int(raw_input('quantity: ')))
del item[-1]

receipt = {'item name':item,'price':price,'quantity':quantity}

print('-'*len('receipt')*2+'\n    receipt\n'+'-'*len('receipt')*2)

total_price = []
for x in range(len(price)):
        total_price.append(price[x]*quantity[x])
        print('%d %s %.3fKD'%(quantity[x],item[x],price[x]))
        x+=1
print('-'*len('receipt')*2)


print('total: %.3fKD'%(sum(total_price)))
