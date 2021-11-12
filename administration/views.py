
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect 
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from administration.models import user_details,package_details,hospital_details,cab_details,hotel_details,medical_details,petrol_details,place_details,railway_details,bus_details,hotel_booking,cab_booking,rating,cab_rating,app_rating,package_booking,package_review,blog,coupon
from administration.forms import UserForm,UserForm2
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import pickle
import pandas as pd

# Create your views here.
def user_login(request):
	count=app_rating.objects.all().count()
	rate_sum=app_rating.objects.aggregate(Sum('rating'))
	total=int(rate_sum["rating__sum"])/int(count)
	final_rating=int(total)
	# print("vvv",int(total))
	if request.method == 'POST':
		
		user_name=request.POST.get('username')
		pass_word=request.POST.get('password')
		designation=request.POST.get('designation')
		current_user=1
		user = authenticate(username=user_name, password=pass_word)
		if user:
			login(request,user)
			current_user=request.user.id
		
		if User.objects.values_list('is_superuser', flat=True).get(pk=current_user)==1:

			if designation=='1':
				if user:
					login(request,user)
					return HttpResponseRedirect('/admin_management')
				else:
					return render(request,'administration/login.html')
			else:
				return render(request,'administration/login.html')
		else:

			if designation=='0':
				if request.user.last_name=="user":
					if user:
						login(request,user)
						return HttpResponseRedirect('/user_management')
					else:
						return render(request,'administration/login.html')
				else:
					return render(request,'administration/login.html')
			if designation=='2':
				if request.user.last_name=="store":
					if user:
						login(request,user)
						return HttpResponseRedirect('/store_management')
					else:
						return render(request,'administration/login.html')
				else:
					return render(request,'administration/login.html')
		
		
	return render(request,'administration/login.html',{'final_rating':final_rating})

def user_logout(request):
	
	logout(request)
	return HttpResponseRedirect('/')

def registration(request):
	form=UserForm()
		# form2=create_staffs()
	if request.method == 'POST':
		
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/registration')
	else:

		form=UserForm()

		
	return render(request,'administration/register.html',{'form':form})



@login_required(login_url='/')
def admin_management(request):
	return render(request,'administration/add_package.html')




@login_required(login_url='/')
def add_package(request):
	if request.method == 'POST':
		
		cre_package=package_details(
		package_name=request.POST['packagename'],
		kilometers=request.POST['total_km'],

		)
		cre_package.save()
		package_id=package_details.objects.values_list('pk', flat=True).latest('id')
		count=request.POST['count']
		if count=="0":
			cre_places=place_details(
				pacakge_id=package_id,
				place=request.POST['place0'],
				location=request.POST['location0'],
				pincode=request.POST['pincode0'],
				kilometers=request.POST['km0'],
				kilometers_more=request.POST['kmm0']
	
				)
			cre_places.save()
		else:
			for cc in range(0,int(count)+1):
				cre_places=place_details(
					pacakge_id=package_id,
					place=request.POST['place%d'%cc],
					location=request.POST['location%d'%cc],
					pincode=request.POST['pincode%d'%cc],
				
					kilometers=request.POST['km%d'%cc],
					kilometers_more=0
					)
				cre_places.save()
	return render(request,'administration/add_package.html')

@login_required(login_url='/')
def recomendation(request):
	blogs=blog.objects.filter(status="pending")
	place=[]
	comment=[]
	package_id=[]
	location=[]
	sentiment=[]
	for x in blogs:	
		place.append(x.place)
		comment.append(x.comment)
		package_id.append(x.package_id)
		location.append(x.location)
	model = pickle.load(open("tourmodel", 'rb'))
	for y in comment:
		result = model.predict([y])
		if result==["not happy"]:
			sentiment.append(0)
		else:
			sentiment.append(1)

	df= pd.DataFrame({"place": place,"comment": comment,"sentiment":sentiment,"package_id":package_id,"location":location})
	result = df.groupby(['place','package_id','location'], as_index=False).agg({'sentiment': 'sum'})
	result['count'] = df.groupby('place')['place'].transform('count')
	result = result[result['sentiment'] >=5]  
	result['avg'] = result['sentiment']/result['count']
	result=result[result['avg'] >=.5]  

	rc_place=[]
	rc_package_id=[]
	rc_package_name=[]
	rc_location=[]
	# package_details.objects.values_list('package_name', flat=True).get(pk=id)
	print(result)
	for x,y,z in zip(result['place'],result['package_id'],result['location']):
		rc_place.append(x)
		rc_package_id.append(y)
		rc_package_name.append(package_details.objects.values_list('package_name', flat=True).get(pk=y))
		rc_location.append(z)
	recom=zip(rc_place,rc_package_id,rc_package_name,rc_location)
	return render(request,'administration/recomendation.html',{"recom":recom})

@login_required(login_url='/')
def add_recomendation(request):
	if request.method == 'POST':
		cre_places=place_details(
			pacakge_id=request.POST['pacakge_id'],
			place=request.POST['place'],
			location=request.POST['location'],
			pincode=request.POST['pincode'],
			kilometers=request.POST['kilometer'],
			kilometers_more=0
			)
		cre_places.save()
		blog.objects.filter(place=request.POST['place']).update(status="done")
	return HttpResponseRedirect('/admin_management')
@login_required(login_url='/')
def delete_recomendation(request):
	if request.method == 'POST':
		blog.objects.filter(place=request.POST['place']).update(status="done")
	return HttpResponseRedirect('/admin_management')

@login_required(login_url='/')
def add_hospital(request):
	if request.method == 'POST':
		
		cre_hospital=hospital_details(
			name=request.POST['hospitaname'],
			location=request.POST['hospitallocation'],
			pincode=request.POST['hospitalpincode'],
			)
		cre_hospital.save()

	return render(request,'administration/add_hospital.html')
@login_required(login_url='/')
def add_hotels(request):
	form=UserForm()
	if request.method == 'POST':
		
		cre_hotel=hotel_details(
			name=request.POST['hotelname'],
			location=request.POST['hotellocation'],
			pincode=request.POST['hotelpincode'],
			roomsavailable=request.POST['roomsavailable'],
			)
		cre_hotel.save()
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			usr=User.objects.latest('id')
			User.objects.get(id=usr.id).update(last_name="store")
			return HttpResponseRedirect('/admin_management')
		else:
			form=UserForm()
		
	return render(request,'administration/add_hotels.html',{'form':form})
@login_required(login_url='/')
def add_medical(request):
	if request.method == 'POST':
		
		cre_medical=medical_details(
			name=request.POST['medicalname'],
			location=request.POST['medicallocation'],
			pincode=request.POST['medicalpincode'],
			)
		cre_medical.save()
	return render(request,'administration/add_medical.html')
@login_required(login_url='/')
def add_petrol(request):
	if request.method == 'POST':
		
		cre_petrol=petrol_details(
			name=request.POST['petrolname'],
			location=request.POST['petrollocation'],
			pincode=request.POST['petrolpin'],
			)
		cre_petrol.save()
	return render(request,'administration/add_petrol.html')

@login_required(login_url='/')
def add_cab(request):
	if request.method == 'POST':
		
		cre_cab=cab_details(
			name=request.POST['cabaname'],
			phone=request.POST['cabphone'],
			location=request.POST['cablocation'],
			pincode=request.POST['cabpincode'],

			)
		cre_cab.save()
	return render(request,'administration/add_cab.html')
@login_required(login_url='/')
def add_railway(request):
	if request.method == 'POST':
		
		cre_cab=railway_details(
			name=request.POST['name'],
			phone=request.POST['phone'],
			location=request.POST['location'],
			pincode=request.POST['pincode'],

			)
		cre_cab.save()
	return render(request,'administration/add_railway.html')
@login_required(login_url='/')
def add_bus(request):
	if request.method == 'POST':
		
		cre_cab=bus_details(
			name=request.POST['name'],
			phone=request.POST['phone'],
			location=request.POST['location'],
			pincode=request.POST['pincode'],

			)
		cre_cab.save()
	return render(request,'administration/add_bustand.html')




@login_required(login_url='/')
def view_package(request):
	details=package_details.objects.all().order_by('-id')
	
	return render(request,'administration/admin_view_package.html',{'details':details})
@login_required(login_url='/')
def view_user(request):
	details=User.objects.all().order_by('-id')
	
	return render(request,'administration/admin_view_user.html',{'details':details})
@login_required(login_url='/')
def individual_view_package(request,id):
	pack_details=package_details.objects.get(pk=id)
	place_det=place_details.objects.all().filter(pacakge_id=id)
	
	return render(request,'administration/event_planner_admin.html',{'pack_details':pack_details,'place_det':place_det})
@login_required(login_url='/')
def view_hospital(request):
	details=hospital_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_hospital.html',{'details':details})
@login_required(login_url='/')
def view_hotels(request):
	details=hotel_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_hotel.html',{'details':details})
@login_required(login_url='/')
def view_medical(request):
	details=medical_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_medical.html',{'details':details})
@login_required(login_url='/')
def view_petrol(request):
	details=petrol_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_petrol.html',{'details':details})
@login_required(login_url='/')
def view_cab(request):
	details=cab_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_cab.html',{'details':details})
@login_required(login_url='/')
def view_railway(request):
	details=railway_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_railway.html',{'details':details})
@login_required(login_url='/')
def view_bus(request):
	details=bus_details.objects.all().order_by('-id')

	return render(request,'administration/admin_view_bustand.html',{'details':details})

@login_required(login_url='/')
def user_management(request):
	last_five = package_details.objects.all().order_by('-id')[:6]
	full = package_details.objects.all().order_by('-id')
	return render(request,'user/userhome.html',{'last_five':last_five,'full':full})


@login_required(login_url='/')
def select_places(request,id):
	pack_details=package_details.objects.get(pk=id)
	pack_id=id
	place_det=place_details.objects.all().filter(pacakge_id=id)
	full = package_details.objects.all().order_by('-id')
	return render(request,'user/packagebooking.html',{'pack_details':pack_details,'place_det':place_det,"full":full,'pack_id':pack_id})

@login_required(login_url='/')
def event_planner_user(request,id):
	place_ids=[]
	loops=request.POST['loop']
	for x in range(1,int(loops)+1):
		if request.POST.get('checked_place{}'.format(x))!=None:
			place_ids.append(request.POST.get('checked_place{}'.format(x)))
			# place_det=place_details.objects.all().filter(pacakge_id=id)
	# return HttpResponse(place_ids)
	kilme=[]
	hotel_links=[]
	cab_links=[]
	hospital_links=[]
	medical_links=[]
	railway_links=[]
	bus_links=[]
	petrol_links=[]

	hotel_pincode=[]
	cab_pincode=[]
	hospital_pincode=[]
	medical_pincode=[]
	railway_pincode=[]
	bus_pincode=[]
	petrol_pincode=[]

	search_links=[]
	pincodes=[]

	pack_details=package_details.objects.get(pk=id)
	place_det=place_details.objects.all().filter(pk__in=place_ids)


	for kilomm in place_det:
		kilme.append(int(kilomm.kilometers))
	total_km=int(package_details.objects.values_list('kilometers', flat=True).get(pk=id))+sum(kilme)
	cab_detai=cab_details.objects.all()
	hotel_detai=hotel_details.objects.all()
	hospital_detai=hospital_details.objects.all()
	medical_detai=medical_details.objects.all()
	railway_detai=railway_details.objects.all()
	bus_detai=bus_details.objects.all()
	petrol_detai=petrol_details.objects.all()
	#user_id=request.POST['test']


	for x in hotel_detai:
		hotel_links.append('<a href="../details_hotels/{}">{}-Hotel</a>'.format(x.id,x.name))
		hotel_pincode.append(x.pincode)
	for y in cab_detai:
		cab_links.append('<a href="../details_cab/{}">{}-Cab</a>'.format(y.id,y.name))
		cab_pincode.append(y.pincode)
	for y in hospital_detai:
		hospital_links.append('<a href="../details_hospital/{}">{}-Hospital</a>'.format(y.id,y.name))
		hospital_pincode.append(y.pincode)
	for y in medical_detai:
		medical_links.append('<a href="../details_medical/{}">{}-Medicalstore</a>'.format(y.id,y.name))
		medical_pincode.append(y.pincode)
	for y in railway_detai:
		railway_links.append('<a href="../details_railway/{}">{}-Railway</a>'.format(y.id,y.name))
		railway_pincode.append(y.pincode)
	for y in bus_detai:
		bus_links.append('<a href="../details_bus/{}">{}-Bus</a>'.format(y.id,y.name))
		bus_pincode.append(y.pincode)
	for y in petrol_detai:
		petrol_links.append('<a href="../details_petrol/{}">{}-Petrolpumps</a>'.format(y.id,y.name))
		petrol_pincode.append(y.pincode)
	search_links=hotel_links+cab_links+hospital_links+medical_links+railway_links+bus_links+petrol_links
	pincodes=hotel_pincode+cab_pincode+hospital_pincode+medical_pincode+railway_pincode+bus_pincode+petrol_pincode
	
	return render(request,'user/eventplanner.html',{'pack_details':pack_details,'place_det':place_det,'zipped':list(zip(search_links,pincodes)),'total_km':total_km})

@login_required(login_url='/')
def user_view_booked_package(request):
	boking=package_booking.objects.filter(user_id=request.user.id)
	details=package_details.objects.all()
	
	return render(request,'user/packagebookinglist.html',{'details':details,'boking':boking})

@login_required(login_url='/')
def user_view_package(request):
	details=package_details.objects.all().order_by('-id')
	
	return render(request,'user/packages.html',{'details':details})


@login_required(login_url='/')
def package_detail(request,id):
	detail=package_details.objects.get(pk=id)
	place_detail=place_details.objects.filter(pacakge_id=id)
	review=package_review.objects.filter(package_id=id)
	if review:
		rat=[]
	else:
		rat=[0]
	for x in review:
		rat.append(float(x.rating))
	from statistics import mean
	rating=mean(rat)

	return render(request,'user/packagedetail.html',{'detail':detail,'place_detail':place_detail,'review':review,'totrat':round(rating, 2)})

@login_required(login_url='/')
def add_review(request,id):
	if request.method == 'POST':
		review=package_review(
		package_id=id,
		user_id=request.user.id,
		rating=request.POST['rating'],
		comment=request.POST['review']
		)
		review.save()
	return HttpResponseRedirect('/package_detail/{}'.format(id))

@login_required(login_url='/')
def book_tour(request,id):
	book=package_booking(
	package_id=id,
	user_id=request.user.id,
	)
	book.save()
	book_id = package_booking.objects.latest('id')
	copn=coupon(
	booking_id=book_id.id,
	store_id=1,
	status="notused"
	)
	copn.save()
	return HttpResponseRedirect('/coupons/{}'.format(id))

@login_required(login_url='/')
def coupons(request,id):
	details=package_details.objects.get(pk=id)
	book_id = package_booking.objects.latest('id')
	usr=User.objects.all()
	return render(request,'user/coupon.html',{'details':details,'book_id':book_id,'usr':usr})

@login_required(login_url='/')
def user_view_booking(request):
	user_det=User.objects.get(pk=request.user.id)
	hotel_book=hotel_booking.objects.filter(user_ref_id=request.user.id)
	hotel_detai=hotel_details.objects.all()
	cab_book=cab_booking.objects.filter(user_ref_id=request.user.id)
	return render(request,'user/hotelandcab.html',{'user_det':user_det,'hotel_book':hotel_book,
		'hotel_detai':hotel_detai,'cab_book':cab_book})

@login_required(login_url='/')
def view_blog(request):
	details=package_details.objects.all().order_by("-id")
	blogdet=blog.objects.all().order_by("-id")
	return render(request,'user/blog-nosidebar.html',{'details':details,'blogdet':blogdet})

@login_required(login_url='/')
def add_blog(request):
	if request.method == 'POST':
		lat=request.POST['lat']
		log=request.POST['log']
		location="http://maps.google.com/?q={},{}".format(lat,log)
		blogs=blog.objects.filter(place=request.POST['place'],status="done")

		if not blogs:
			blogs=blog(
			package_id=request.POST['pack_id'],
			user_id=request.user.id,
			pic=request.FILES['pic'],
			place=request.POST['place'],
			location=location,
			comment=request.POST['comnt'],
			status="pending"
			)
			blogs.save()
			blog.objects.filter(place=request.POST['place']).update(location=location)
		else:
			blogs=blog(
			package_id=request.POST['pack_id'],
			user_id=request.user.id,
			pic=request.FILES['pic'],
			place=request.POST['place'],
			location=location,
			comment=request.POST['comnt'],
			status="done"
			)
			blogs.save()
	return HttpResponseRedirect('/view_blog')

@login_required(login_url='/')
def user_search_package(request):
	if request.method == 'POST':
	
		search_result=request.POST.get('searches')
	details=package_details.objects.filter(package_name__contains=search_result)
	
	return render(request,'administration/user_view_packages.html',{'details':details})
@login_required(login_url='/')
def details_hotels(request,id):
	details=hotel_details.objects.get(pk=id)
	ratings=rating.objects.filter(hotel_ref=id)
	return render(request,'administration/individual_details_with_booking.html',{'details':details,'id':id,'ratings':ratings})
@login_required(login_url='/')
def details_cab(request,id):
	details=cab_details.objects.get(pk=id)
	ratings=cab_rating.objects.filter(cab_ref=id)
	return render(request,'administration/individual_details_booking_cab.html',{'details':details,'id':id,'ratings':ratings})
@login_required(login_url='/')
def details_hospital(request,id):
	details=hospital_details.objects.get(pk=id)

	return render(request,'administration/individual_details.html',{'details':details,'id':id})
@login_required(login_url='/')
def details_medical(request,id):
	details=medical_details.objects.get(pk=id)

	return render(request,'administration/individual_details.html',{'details':details,'id':id})
@login_required(login_url='/')
def details_petrol(request,id):
	details=petrol_details.objects.get(pk=id)

	return render(request,'administration/individual_details.html',{'details':details,'id':id})

@login_required(login_url='/')
def details_railway(request,id):
	details=railway_details.objects.get(pk=id)

	return render(request,'administration/individual_details.html',{'details':details,'id':id})
@login_required(login_url='/')
def details_bus(request,id):
	details=bus_details.objects.get(pk=id)

	return render(request,'administration/individual_details.html',{'details':details,'id':id})

@login_required(login_url='/')
def book_hotel(request,id):
	details=hotel_details.objects.get(pk=id)
	
	return render(request,'administration/hotel_booking.html',{'details':details})
@login_required(login_url='/')
def save_hotel_book(request,id):
	hotel_nam=hotel_details.objects.values_list('name', flat=True).get(pk=id)
	cre_hotel_book=hotel_booking(
		hotel_ref_id=id,
		hotel_name=hotel_nam,
		user_ref_id=request.user.id,
		check_in=request.POST['check_in'],
		check_out=request.POST['check_out'],
		no_of_rooms=request.POST['no_of_rooms'],
		total_persons=request.POST['no_of_person'],
		)
	cre_hotel_book.save()
	user_det=User.objects.get(pk=request.user.id)
	latest_booking=hotel_booking.objects.values_list('pk', flat=True).latest('id')

	return render(request,'administration/hotel_confirm.html',{'user_det':user_det,'bookin_id':int(latest_booking)+1,
		'check_in':request.POST['check_in'],'check_out':request.POST['check_out'],'no_of_rooms':request.POST['no_of_rooms'],'no_of_persons':request.POST['no_of_person']})
@login_required(login_url='/')
def book_cab(request,id):
	details=cab_details.objects.get(pk=id)
	return render(request,'administration/cab_book.html',{'details':details})
@login_required(login_url='/')
def save_cab_book(request,id):
	cab_nam=cab_details.objects.values_list('name', flat=True).get(pk=id)
	cre_hotel_book=cab_booking(
		cab_ref_id=id,
		cab_name=cab_nam,
		user_ref_id=request.user.id,
		date=request.POST['date'],
		time=request.POST['time'],
		no_of_cab=request.POST['no_of_cabs'],
		total_persons=request.POST['no_of_person'],
		)
	cre_hotel_book.save()
	user_det=User.objects.get(pk=request.user.id)
	latest_booking=cab_booking.objects.values_list('pk', flat=True).latest('id')
	return render(request,'administration/cab_confirm.html',{'user_det':user_det,'bookin_id':int(latest_booking)+1,
		'date':request.POST['date'],'time':request.POST['time'],'no_of_cabs':request.POST['no_of_cabs'],'total_persons':request.POST['no_of_person']})

@login_required(login_url='/')
def add_rating_hotel(request,id):
	cre_rate=rating(
		user_name=User.objects.values_list('username', flat=True).get(pk=request.user.id),
		hotel_ref=id,
		rating=request.POST['rate'],
		review=request.POST['review'],
		)
	cre_rate.save()
	
	return HttpResponseRedirect('/details_hotels/{}'.format(id))
@login_required(login_url='/')
def add_rating_cab(request,id):
	cre_rate=cab_rating(
		user_name=User.objects.values_list('username', flat=True).get(pk=request.user.id),
		cab_ref=id,
		rating=request.POST['rate'],
		review=request.POST['review'],
		)
	cre_rate.save()
	return HttpResponseRedirect('/details_cab/{}'.format(id))


# def edit_package(request,id):
# 	details=hotel_details.objects.get(pk=id)
# 	return render(request,'administration/edit_hotels.html',{'details':details})
# def update_package(request,id):
# 	hotel_update=hotel_details.objects.get(pk=id)
# 	hotel_update.name=request.POST['hotelname']
# 	hotel_update.location=request.POST['hotellocation']
# 	hotel_update.pincode=request.POST['hotelpincode']
# 	hotel_update.roomsavailable=request.POST['roomsavailable']
# 	hotel_update.save()
# 	return HttpResponseRedirect('/view_hotels')
@login_required(login_url='/')
def delete_package(request,id):
	package_delete=package_details.objects.get(pk=id)
	place_delete=place_details.objects.filter(pacakge_id=id)
	package_delete.delete()
	place_delete.delete()
	return HttpResponseRedirect('/view_package')

@login_required(login_url='/')
def edit_hotel(request,id):
	details=hotel_details.objects.get(pk=id)
	return render(request,'administration/edit_hotels.html',{'details':details})
@login_required(login_url='/')
def update_hotel(request,id):
	hotel_update=hotel_details.objects.get(pk=id)
	hotel_update.name=request.POST['hotelname']
	hotel_update.location=request.POST['hotellocation']
	hotel_update.pincode=request.POST['hotelpincode']
	hotel_update.roomsavailable=request.POST['roomsavailable']
	hotel_update.save()
	return HttpResponseRedirect('/view_hotels')
@login_required(login_url='/')
def delete_hotel(request,id):
	hotel_delete=hotel_details.objects.get(pk=id)
	hotel_delete.delete()
	return HttpResponseRedirect('/view_hotels')
@login_required(login_url='/')
def edit_bustand(request,id):
	details=bus_details.objects.get(pk=id)
	return render(request,'administration/edit_bustand.html',{'details':details})
@login_required(login_url='/')
def update_bustand(request,id):
	bustand_update=bus_details.objects.get(pk=id)
	bustand_update.name=request.POST['bus_name']
	bustand_update.location=request.POST['bus_location']
	bustand_update.phone=request.POST['bus_phone']
	bustand_update.pincode=request.POST['bus_pincode']
	
	bustand_update.save()
	return HttpResponseRedirect('/view_bus')
@login_required(login_url='/')
def delete_bus(request,id):
	bus_delete=bus_details.objects.get(pk=id)
	bus_delete.delete()
	return HttpResponseRedirect('/view_bus')

@login_required(login_url='/')
def edit_cab(request,id):
	details=cab_details.objects.get(pk=id)
	return render(request,'administration/edit_cab.html',{'details':details})
@login_required(login_url='/')
def update_cab(request,id):
	cab_update=cab_details.objects.get(pk=id)
	cab_update.name=request.POST['cabname']
	cab_update.location=request.POST['cablocation']
	cab_update.phone=request.POST['cabphone']
	cab_update.pincode=request.POST['cabpincode']
	
	cab_update.save()
	return HttpResponseRedirect('/view_cab')

@login_required(login_url='/')
def delete_cab(request,id):
	cab_delete=cab_details.objects.get(pk=id)
	cab_delete.delete()

	return HttpResponseRedirect('/view_cab')


@login_required(login_url='/')
def edit_hospital(request,id):
	details=hospital_details.objects.get(pk=id)
	return render(request,'administration/edit_hospital.html',{'details':details})
@login_required(login_url='/')
def update_hospital(request,id):
	hstl_update=hospital_details.objects.get(pk=id)
	hstl_update.name=request.POST['hospitaname']
	hstl_update.location=request.POST['hospitallocation']

	hstl_update.pincode=request.POST['hospitalpincode']
	
	hstl_update.save()
	return HttpResponseRedirect('/view_hospital')

@login_required(login_url='/')
def delete_hospital(request,id):
	cab_delete=hospital_details.objects.get(pk=id)
	cab_delete.delete()

	return HttpResponseRedirect('/view_hospital')
@login_required(login_url='/')
def edit_petrol(request,id):
	details=petrol_details.objects.get(pk=id)
	return render(request,'administration/edit_petrol.html',{'details':details})
@login_required(login_url='/')
def update_petrol(request,id):
	ptl_update=petrol_details.objects.get(pk=id)
	ptl_update.name=request.POST['petrolname']
	ptl_update.location=request.POST['petrollocation']

	ptl_update.pincode=request.POST['petrolpin']
	
	ptl_update.save()
	return HttpResponseRedirect('/view_petrol')

@login_required(login_url='/')
def delete_petrol(request,id):
	cab_delete=petrol_details.objects.get(pk=id)
	cab_delete.delete()

	return HttpResponseRedirect('/view_petrol')

@login_required(login_url='/')
def edit_medical(request,id):
	details=medical_details.objects.get(pk=id)
	return render(request,'administration/edit_medical.html',{'details':details})
@login_required(login_url='/')
def update_medical(request,id):
	mdl_update=medical_details.objects.get(pk=id)
	mdl_update.name=request.POST['medicalname']
	mdl_update.location=request.POST['medicallocation']

	mdl_update.pincode=request.POST['medicalpincode']
	
	mdl_update.save()
	return HttpResponseRedirect('/view_medical')

@login_required(login_url='/')
def delete_medical(request,id):
	med_delete=medical_details.objects.get(pk=id)
	med_delete.delete()

	return HttpResponseRedirect('/view_medical')
@login_required(login_url='/')
def edit_railway(request,id):
	details=railway_details.objects.get(pk=id)
	return render(request,'administration/edit_railway.html',{'details':details})
@login_required(login_url='/')
def update_railway(request,id):
	rail_update=railway_details.objects.get(pk=id)
	rail_update.name=request.POST['name']
	rail_update.location=request.POST['location']
	rail_update.phone=request.POST['phone']

	rail_update.pincode=request.POST['pincode']
	
	rail_update.save()
	return HttpResponseRedirect('/view_railway')

@login_required(login_url='/')
def delete_railway(request,id):
	med_delete=railway_details.objects.get(pk=id)
	med_delete.delete()

	return HttpResponseRedirect('/view_railway')
@login_required(login_url='/')
def rate_app(request):

	return render(request,'administration/app_rating.html')
@login_required(login_url='/')
def submit_rating(request):
	rating=request.POST['rate']
	review=request.POST['review']

	app_rate=app_rating(
		rating=request.POST['rate'],
		review=request.POST['review'],
		)
	app_rate.save()
	
	return HttpResponseRedirect('/user_management')


@login_required(login_url='/')
def delete_user(request,id):
	med_delete=User.objects.get(pk=id)
	med_delete.delete()

	return HttpResponseRedirect('/view_user')

@login_required(login_url='/')
def store_management(request):
	return render(request,'store/store_home.html')

@login_required(login_url='/')
def coupon_list(request):
	coupn=coupon.objects.all()
	return render(request,'store/coupon_list.html',{'coupn':coupn})

@login_required(login_url='/')
def coupon_usage(request,id):
	coupon_update=coupon.objects.get(pk=id)
	coupon_update.store_id=request.user.id
	coupon_update.status="used"
	coupon_update.save()
	return HttpResponseRedirect('/coupon_list')