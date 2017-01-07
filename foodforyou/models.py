from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.
CUISINE = (
			('AFG','Afghani'), ('ARB','Arabian'), ('ASM','Assamese'), ('AWD','Awadhi'), ('BNG','Bengali'), ('CHN','Chinese'), ('CNT','Continental'), 
			('DSR','Dessserts'), ('FRN','French'), ('GUJ','Gujarati'), ('HYD','Hyderabadi'), ('ITL','Italian'), ('JPN','Japanese'), ('KSH','Kashmiri'),
			('KOR','Korean'), ('LEB','Lebanese'), ('MEX','Mexican'), ('NRI','North Indian'), ('RAJ','Rajasthani'), ('SIN','Sindhi'), ('SOI','South Indian'), 
			('THI','Thai')
		)
TIME = (
		('000','00:00'), ('001','01:00'), ('002','02:00'),('003','03:00'),('004','04:00'),('005','05:00'),('006','06:00'),('007','07:00'),('008','08:00'),('009','09:00'),('010','10:00'),('011','11:00'),('012','12:00'),('013','13:00'),('014','14:00'),('015','15:00'),('016','16:00'),('017','17:00'),('018','18:00'),('019','19:00'),('020','20:00'),('021','21:00'),('022','22:00'),('023','23:00')
	)
	
STATUS = (
		('PL','Placed'), ('ON','Ongoing'), ('DP','Dispatched'), ('DL','Delivered')
	)
def generateUUID():
	return str(uuid4())

class User(models.Model):
	user_id = models.UUIDField(primary_key=True, default=generateUUID, editable= False)
	name = models.CharField(max_length=50)
	phone_num = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class Restaurant(models.Model):
	restro_id= models.UUIDField(primary_key=True, default=generateUUID, editable=False)
	name = models.CharField(max_length=100)
	address=models.CharField(max_length=200)
	city=models.CharField(max_length=50)
	pincode=models.IntegerField()
	phone_num=models.CharField(max_length=10)
	email=models.CharField(max_length=50)
	website= models.CharField(max_length=50)
	cuisine = models.CharField(max_length=50, default='SELECT', choices=CUISINE)
	time_start = models.CharField(max_length=50, default='SELECT', choices=TIME)
	time_end = models.CharField(max_length=50, default='SELECT', choices=TIME)
	
class Menus(models.Model):
	restro_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	menu_id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
	category = models.CharField(max_length = 50)
	
class Items(models.Model):
	item_id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
	name = models.CharField(max_length=50)
	price = models.IntegerField()
	
class JoinTable(models.Model):
	restro_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	menu_id = models.ForeignKey(Menus, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
	
class Orders(models.Model):
	order_id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	order_amount = models.IntegerField()
	address = models.CharField(max_length=200)
	date = models.DateField(auto_now_add=True)
	
class Cart(models.Model):
	id = models.AutoField(primary_key=True)
	order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
	quantity = models.IntegerField(default='1')
	amount = models.IntegerField(default='00')
	
class ManageOrder(models.Model):
	id = models.AutoField(primary_key=True)
	restro_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, default='Placed', choices=STATUS)
	