
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
from administration.models import user_details,package_details,hospital_details,cab_details,hotel_details,medical_details,petrol_details,place_details,railway_details,bus_details,hotel_booking,cab_booking,rating,cab_rating,app_rating
from administration.forms import UserForm,UserForm2
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

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
				if user:
					login(request,user)
					return HttpResponseRedirect('/user_management')
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
			return HttpResponse('User registered')
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
					kilometers_more=request.POST['kmm%d'%cc]
					)
				cre_places.save()
	return render(request,'administration/add_package.html')
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
	if request.method == 'POST':
		
		cre_hotel=hotel_details(
			name=request.POST['hotelname'],
			location=request.POST['hotellocation'],
			pincode=request.POST['hotelpincode'],
			roomsavailable=request.POST['roomsavailable'],
			)
		cre_hotel.save()
	return render(request,'administration/add_hotels.html')
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
	last_five = package_details.objects.all().order_by('-id')[:5]
	full = package_details.objects.all().order_by('-id')
	return render(request,'administration/user_home.html',{'last_five':last_five,'full':full})
@login_required(login_url='/')
def select_places(request,id):
	pack_details=package_details.objects.get(pk=id)
	pack_id=id
	place_det=place_details.objects.all().filter(pacakge_id=id)
	full = package_details.objects.all().order_by('-id')
	return render(request,'administration/create_places.html',{'pack_details':pack_details,'place_det':place_det,"full":full,'pack_id':pack_id})

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
	
	return render(request,'administration/event_planner_user.html',{'pack_details':pack_details,'place_det':place_det,'zipped':list(zip(search_links,pincodes)),'total_km':total_km})
@login_required(login_url='/')
def user_view_package(request):
	details=package_details.objects.all().order_by('-id')
	
	return render(request,'administration/user_view_packages.html',{'details':details})
@login_required(login_url='/')
def user_view_booking(request):
	user_det=User.objects.get(pk=request.user.id)
	hotel_book=hotel_booking.objects.filter(user_ref_id=request.user.id)
	hotel_detai=hotel_details.objects.all()
	cab_book=cab_booking.objects.filter(user_ref_id=request.user.id)
	return render(request,'administration/user_view_bookings.html',{'user_det':user_det,'hotel_book':hotel_book,
		'hotel_detai':hotel_detai,'cab_book':cab_book})
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