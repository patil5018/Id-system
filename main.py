import mysql.connector
from PIL import Image,ImageDraw,ImageFont

font1=ImageFont.truetype("arial.ttf",30)
font2=ImageFont.truetype("arial.ttf",60)
size=height,width=(700,500)

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="image")
mycursor=mydb.cursor()
#mycursor=conn.cursor()

print("*******************************Welcome to ID Generator********************************")
print("Fill the details:")
id1=input("Enter the employee ID:")
company_name=input("Enter your company name:")
name=input("Name:")
mob1=input("Mob No:")
em=input("Email:")
des=input("Designation:")
age=input("Age:")
bl_grp=input("Blood group:")
Dept=input("Department:")
path1=input("Enter image path:")
mycursor.execute("insert into new_image(company_name,name,ID,mob,email,desig,age,blood,dept) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(company_name,id1,name,mob1,em,des,age,bl_grp,Dept))

#mycursor.execute("INSERT INTO Proj1(email,pri,date1,time1) VALUES(%s, %s, %s , %s)",(ma,fullp,dat,current_time))
mydb.commit();
photo=Image.open(path1)
#print(photo.size)
photo.thumbnail((250,250))

img=Image.new("RGB", size,"WHITE")
#img.show()
img.paste(photo,(60,170))
draw =ImageDraw.Draw(img)
draw.text((100,50),"{}".format(company_name),"Blue",font=font2)
draw.text((330,155),"Employee ID:-{}".format(id1),"black",font=font1)
draw.text((330,220),"Name :-{}".format(name),"black",font=font1)
draw.text((330,290),"Designation: {}".format(des),"black",font=font1)
draw.text((330,360),"Department: {}".format(Dept),"black",font=font1)
draw.text((330,430),"Blood Group: {}".format(bl_grp),"black",font=font1)

img.show()
img.save("E:/image project/{}.png".format(id1))



#create table new_image(company_name varchar(20),name varchar(20),mob int(20),email varchar2(30),desig varchar(30),age int(50),blood varchar2(20),dept varchar(20));
