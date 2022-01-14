import psycopg2
import matplotlib.pyplot as plt 

yOrNoList = input("Linked list, Y/N: ")
yOrNoList.upper()
if yOrNoList == "Y":
	class Node:
		def __init__(self, dataval=None):
			self.dataval = dataval
			self.nextval = None
	class SLinkedList:
		def __init__(self):
			self.headval = None
		def listprint(self):
			printval = self.headval
			while printval is not None:
				print (printval.dataval)
				printval = printval.nextval
	list1 = SLinkedList()
	list1.headval = Node("Mon")
	e2 = Node("Tue")
	e3 = Node("Wed")
	list1.headval.nextval = e2
	e2.nextval = e3
	list1.listprint()
elif yOrNoList == "N":
	yOrNoDB = input("Database, Y/N: ")
	yOrNoDB.upper()
	if yOrNoDB == "Y":
		a = 0
		b = 0
		c = 0
		d = 0
		e = 0
		f = 0
		g = 0
		h = 0
		x = [1,2,3,4,5,6,7,8] #"Male", "Female", "Genderfluid", "Polygender", "Agender", "Genderqueer", "Non-binary", "Bigender"
		try:
			connection = psycopg2.connect(user="postgres",
			password="P@ssW0rd69",
			host="localhost",
			port="5432",
			database="pythonjob")
			cursor = connection.cursor()
			postgreSQL_select_Query = "SELECT * FROM nasa"
			cursor.execute(postgreSQL_select_Query)
			nasa_records = cursor.fetchall()
			for row in nasa_records:
				id = row[0]
				first_name = row[1]
				last_name = row[2]
				email = row[3]
				gender = row[4]
				ipv4 = row[5]
				match gender:
					case "Male":
						a += 1
					case "Female":
						b += 1
					case "Genderfluid":
						c += 1
					case "Polygender":
						d += 1
					case "Agender":
						e += 1
					case "Genderqueer":
						f += 1
					case "Non-binary":
						g += 1
					case "Bigender":
						h += 1
			y = [a,b,c,d,e,f,g,h]
			print(a,b,c,d,e,f,g,h)
			tick_label = ['Male', 'Female', 'Fluid', 'Poly', 'Agender', 'Queer', 'NonBinary', 'Bi']
			plt.bar(x,y,tick_label = tick_label,width = 0.8, color = ['red','pink'])
			plt.xlabel('Genders')
			plt.ylabel('Amount')
			plt.title('Genders and the amount of them')
			plt.show()
		except (Exception, psycopg2.Error) as error:
			print("Error", error)
	elif yOrNoDB == "N":
		print("something else")
	else:
		print("You typed something wrong I can get you back but I'm way too lazy rn")
else:
	print("You typed something wrong I can get you back but I'm way too lazy rn")


