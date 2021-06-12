from django.db import models

# Create your models here.

class Manager(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	#tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('Entering', 'Entering'),
			('Releasing', 'Releasing'),
			)

	manager = models.ForeignKey(Manager, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	#inventory = models.ForeignKey(Inventory, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.product.name


#class Inventory(models.Model):
	#manager = models.ForeignKey(Manager, null=True, on_delete= models.SET_NULL)
	#order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)

	#def total_qty(self):
		#total_qty = 0
		#inventory_items = Order.objects.filter(order_id=self.id)
		#for inventory_item in inventory_items:
			#if order.status == 'Entering':
				#total_qty = (order.qty + total_qty)
			#else:
				#total_qty = (order.qty - total_qty)
		#return total_qty

	#def __str__(self):
		#return self.product.name










