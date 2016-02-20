"""
Columbia W4111 Intro to databases
Homework 2
"""

import sys
from collections import *

def load_data(file_path):
	"""
	This method reads the dataset, and returns a list of rows.
	Each row is a list containing the values in each column.
	"""
	import csv
	with file(file_path) as f:
		dialect = csv.Sniffer().sniff(f.read(2048))
		f.seek(0)
		reader = csv.reader(f, dialect)
		return [l for l in reader]


def q1(data):
	"""
	@param data the output of load_data()
	@return the number of	distinct types of items (by `description` attribute) in this dataset
	"""
	# Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
	n=0
	t=0
	tot=0
	types=set()
	for line in data:
		n+=1
		if n==1:
			i=-1
			for item in line:
				i+=1
				if item.lower() =='description':
					t=i
		else:
#			types=types | set([line[t].lower()])
			types.add(line[t].lower())
			
	return types.__len__()

def q2(data):
	"""
	@param data the output of load_data()
	@return the number of	distinct `vendor`s (by exact string comparison) in this dataset
	"""
	# Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
	n=0
        t=0
        tot=0
        types=set()
        for line in data:
                n+=1
                if n==1:
                        i=-1
                        for item in line:
                                i+=1
                                if item.lower() =='vendor':
                                        t=i
                else:
#                       types=types | set([line[t].lower()])
                        types.add(line[t])

        return types.__len__()



def q3(data):
	"""
	@param data the output of load_data()
	@return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
	"""
	# Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
	# https://docs.python.org/2/tutorial/datastructures.html
	

        n=0
        store=0
        tot=0
	bottle=0
	sales={}
        for line in data:
                n+=1
                if n==1:
                        i=-1
                        for item in line:
                                i+=1
                                if item.lower() =='store':
                                        store=i
				elif item.lower() =='bottle qty':
					bottle=i
                else:
			s1=line[store]
			num=int(line[bottle])
			if s1 in sales:
				sales[s1]=sales[s1]+num
			else:
				sales[s1]=num
	maximum=-1
	stores = sales.keys()
	for item in stores:
		if maximum==-1:
			maximum=item
		if sales[maximum]<sales[item]:
			maximum=item
        return maximum


def q4(data):
	"""
	@param data the output of load_data()
	@return The value of the `description` attribute of the most sold item from the store from q3()
	"""
	# Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
	# https://docs.python.org/2/tutorial/datastructures.html
	target= q3(data)
	n=0
        store=0
        tot=0
        bottle=0
	res=''
	maxm=0
	d=0
	sales={}
        for line in data:
                n+=1
                if n==1:
                        i=-1
                        for item in line:
                                i+=1
                                if item.lower() =='store':
                                        store=i
                                elif item.lower() =='bottle qty':
                                        bottle=i
				elif item.lower() =='description':
					d=i
                elif line[store]==target:
			num=int(line[bottle])
			name=line[d]
			if name in sales:
				sales[name]=sales[name]+num
			else: 
				sales[name]=num
        wine = sales.keys()
        for item in wine:
                if maxm==0:
                        res=item
			maxm=sales[item]
                if maxm<sales[item]:
                        res=item
			maxm=sales[item]
	return res

def q5(data):
	"""
	Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
	@param data the output of load_data()
	@return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
	"""
	# Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
	# https://docs.python.org/2/tutorial/datastructures.html
	n=0
        zipcode=0
        tot=0
        bottle=0
        res=''
        maxm=0
        cate=0
        sales={}
        for line in data:
                n+=1
                if n==1:
                        i=-1
                        for item in line:
                                i+=1
                                if item.lower() =='zipcode':
                                        zipcode=i
                                elif item.lower() =='bottle qty':
                                        bottle=i
                                elif item.lower() =='category name':
                                        cate=i
                elif line[cate]=='TEQUILA':
			num=int(line[bottle])
			z=line[zipcode]
			if z in sales:
				sales[z]=sales[z]+num
			else:
				sales[z]=num
	maxm=0
	zips=sales.keys()
        for item in zips:
                if maxm==0:
                        res=item
                        maxm=sales[item]
                if maxm<sales[item]:
                        res=item
                        maxm=sales[item]
        return res


if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
		sys.exit(1)
	file_path = sys.argv[1]

	data = load_data(file_path)
	print q1(data)
	print q2(data)
	print q3(data)
	print q4(data)
	print q5(data)

