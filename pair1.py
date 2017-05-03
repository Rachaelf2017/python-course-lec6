
import csv
import sys

f=open('shiller_2013.csv')
my_list= []
reader = csv.reader(f)
for row in reader:
    my_list.append(row)
my_dict ={}
for i in my_list:
    my_dict[i[0]] = i[1]


# print my_dict.values()


my_dict = [price for price in my_dict.values() if float(price[1]) >140]

#gotta get the list to be the right data type
#the dictionary was one step too far

print my_dict
    #
    # landmark_lookup = {}
    # for landmark in index:
    #     if len(landmark) == 2:
    #         landmark_lookup[landmark[0]] = landmark[1]
