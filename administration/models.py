from django.db import models

# Create your models here.
class user_details(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=30)


class package_details(models.Model):
	package_name=models.CharField(max_length=30)

	kilometers=models.CharField(max_length=10)
class place_details(models.Model):
	pacakge_id=models.CharField(max_length=15)
	place=models.CharField(max_length=30)
	location=models.TextField()
	pincode=models.CharField(max_length=30)
	kilometers=models.CharField(max_length=10)
	kilometers_more=models.CharField(max_length=10)

class package_booking(models.Model):
	package_id=models.CharField(max_length=10)
	user_id=models.CharField(max_length=10)

class package_review(models.Model):
	package_id=models.CharField(max_length=10)
	user_id=models.CharField(max_length=10)
	rating=models.CharField(max_length=30)
	comment=models.TextField()

class blog(models.Model):
	package_id=models.CharField(max_length=10)
	user_id=models.CharField(max_length=10)
	pic=models.ImageField(upload_to='blogs/')
	comment=models.TextField()

class hotel_details(models.Model):
	name=models.CharField(max_length=30)
	location=models.TextField()
	pincode=models.CharField(max_length=30)
	roomsavailable=models.CharField(max_length=30)


class hospital_details(models.Model):
	name=models.CharField(max_length=30)
	location=models.TextField()
	pincode=models.CharField(max_length=30)

class cab_details(models.Model):
	name=models.CharField(max_length=30)
	phone=models.CharField(max_length=30)
	location=models.TextField()
	pincode=models.CharField(max_length=30)


class medical_details(models.Model):
	name=models.CharField(max_length=30)
	location=models.TextField()
	pincode=models.CharField(max_length=30)

class petrol_details(models.Model):
	name=models.CharField(max_length=30)
	location=models.TextField()
	pincode=models.CharField(max_length=30)


class railway_details(models.Model):
	name=models.CharField(max_length=30)
	location=models.TextField()
	phone=models.CharField(max_length=30)
	pincode=models.CharField(max_length=30)

class bus_details(models.Model):
	name=models.CharField(max_length=30)
	location=models.TextField()
	phone=models.CharField(max_length=30)
	pincode=models.CharField(max_length=30)


class hotel_booking(models.Model):
	hotel_ref_id=models.CharField(max_length=10)
	hotel_name=models.CharField(max_length=30)
	user_ref_id=models.CharField(max_length=10)
	check_in=models.CharField(max_length=15)
	check_out=models.CharField(max_length=15)
	no_of_rooms=models.CharField(max_length=10)
	total_persons=models.CharField(max_length=10)


class cab_booking(models.Model):
	cab_ref_id=models.CharField(max_length=10)
	cab_name=models.CharField(max_length=30)
	user_ref_id=models.CharField(max_length=10)
	date=models.CharField(max_length=15)
	time=models.CharField(max_length=15)
	no_of_cab=models.CharField(max_length=10)
	total_persons=models.CharField(max_length=10)

class rating(models.Model):
	user_name=models.CharField(max_length=10)
	hotel_ref=models.CharField(max_length=10)
	rating=models.CharField(max_length=10)
	review=models.TextField()

class cab_rating(models.Model):
	user_name=models.CharField(max_length=10)
	cab_ref=models.CharField(max_length=10)
	rating=models.CharField(max_length=10)
	review=models.TextField()

class app_rating(models.Model):
	rating=models.CharField(max_length=10)
	review=models.TextField()

class coupon(models.Model):
	booking_id=models.CharField(max_length=10)
	store_id=models.CharField(max_length=10)
	status=models.CharField(max_length=10)