# import urllib.request as request
# import json
# link = "https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP048/106"
# with request.urlopen(link) as response:
# 	data=json.load(response)
# clist=data["responseData"]
# for county in clist:
# 	print(county["site_id"])

# import pandas as pd
# csvdata=pd.read_csv("opendata106N0101.csv")
# print(csvdata)

# import pandas as pd
# csvdata=pd.read_csv("age.csv")
# mid = csvdata["age"].between(15,25)
# print(csvdata.name[mid])

class price:
	def __init__(self, m, d):
		self.maincourse = m
		self.dessert = d
	def compare(self):
		if self.maincourse>self.dessert:
			print("主菜比較貴")
		elif self.maincourse<self.dessert:
			print("甜點比較貴")
		else:
			print("兩者相等")
	def add(self):
		print("總額為：%d" %(self.maincourse + self.dessert))
		
	def show(self):
		print(self.maincourse,self.dessert)
p = price(100,50)
p.show()
p.compare()
p.add()
