from bs4 import BeautifulSoup

def main():
	#'raw_data.html' can only contain a single <table> tag
	# You can test this script by trying the following link:
	#http://www.cboe.com/DelayedQuote/DQBeta.aspx?content=http%3A%2F%2Fwww.cboe.idmanagedsolutions.com%2Fnew%2Findices%2Fquote.html%3FASSET_CLASS%3DIND%26ID_NOTATION%3D8941848
	#I removed alot of HTML-code so that the only thing left was a <table> tag. I also removed the upper two rows that contained header info ('Calls', 'Puts', 'Contract Name', etc.)
	with open('raw_data.html','r') as f:
		raw_data_str=f.read().replace('\n','')

	#Import into BeautifulSoup
	soup=BeautifulSoup(raw_data_str)

	#Find every <tr> tag, i.e. every row
	allrows=soup.find_all('tr')

	#Some headers for readability
	header_str=['CALL','','','PUT','','']
	for col in header_str:
		print(col.ljust(10),end='')
	print('\n')

	#More header crap
	header_str=['C_Bid','C_Ask','C_Vol','Strike','P_Bid','P_Ask','P_Vol']
	for col in header_str:
		print(col.ljust(10),end='')
	print('\n')	

	#Here's the magic
	numeric_data=[]
	for i,single_row in enumerate(allrows):
		numeric_data.append([])
		cols=single_row.find_all('td')
		for j,idx in enumerate([4,5,7,8,13,14,15]):
			number_str=cols[idx-1].text.strip().replace(',','')
			print(number_str.ljust(10),end='')
			try:
				numeric_data[i].append(float(number_str))
			except:
				numeric_data[i].append(float('Nan'))
				pass
		print('\n')

	#Output file
	with open('output.txt','w') as f:
		for col in header_str:
			f.write(col+' ')
		f.write('\n')
		for row in numeric_data:
			for col in row:
				f.write(str(col)+' ')
			f.write('\n')

if __name__=='__main__':
	main()