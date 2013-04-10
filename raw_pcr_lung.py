#!/user/bin/python
filename=raw_input('Enter the name of your file: ')

from Bio import Medline
year_count={}
input= open(filename)
records = Medline.parse(input)
for record in records:
	year = record["DP"].split()[0]
	if year in year_count:
		year_count[year]+=1
	else:
		year_count[year]=1

for x in sorted(year_count):
	print x,'\t',year_count[x]