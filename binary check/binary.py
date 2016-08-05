binary= raw_input()


binary_list = [int(x) for x in binary.split(',')]
new_list=[]
for y in binary_list:
    if len(str(y))==4 :
        if y%5 == 0:
            new_list.append(y)
            print new_list

        else:
            print
    else:
        print

print


1101,1110,4040