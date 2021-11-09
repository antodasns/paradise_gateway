from administration import views
from django.conf.urls import url
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
app_name='administration'
urlpatterns = [
	path('', views.user_login,name='login'),
	url(r'^registration/$', views.registration,name='registration'),
	path('admin_management', views.admin_management,name='admin_management'),
	path('user_logout', views.user_logout,name='user_logout'),
	url(r'^coupons/(?P<id>\d+)$', views.coupons,name='coupons'),
	url(r'^coupon_usage/(?P<id>\d+)$', views.coupon_usage,name='coupon_usage'),

	path('add_package', views.add_package,name='add_package'),
	path('add_hospital', views.add_hospital,name='add_hospital'),
	path('add_hotels', views.add_hotels,name='add_hotels'),
	path('add_medical', views.add_medical,name='add_medical'),
	path('add_petrol', views.add_petrol,name='add_petrol'),
	path('add_cab', views.add_cab,name='add_cab'),
	path('add_railway', views.add_railway,name='add_railway'),
	path('add_bus', views.add_bus,name='add_bus'),

	path('view_package', views.view_package,name='view_package'),
	url(r'^individual_view_package/(?P<id>\d+)$', views.individual_view_package,name='individual_view_package'),
	path('view_hospital', views.view_hospital,name='view_hospital'),
	path('view_user', views.view_user,name='view_user'),
	path('view_hotels', views.view_hotels,name='view_hotels'),
	path('view_medical', views.view_medical,name='view_medical'),
	path('view_petrol', views.view_petrol,name='view_petrol'),
	path('view_cab', views.view_cab,name='view_cab'),
	path('view_railway', views.view_railway,name='view_railway'),
	path('view_bus', views.view_bus,name='view_bus'),

	path('user_management', views.user_management,name='user_management'),
	url(r'^select_places/(?P<id>\d+)$', views.select_places,name='select_places'),
	url(r'^event_planner_user/(?P<id>\d+)$', views.event_planner_user,name='event_planner_user'),
	path('user_view_booked_package', views.user_view_booked_package,name='user_view_booked_package'),
	path('user_view_package', views.user_view_package,name='user_view_package'),
	url(r'^package_detail/(?P<id>\d+)$', views.package_detail,name='package_detail'),
	url(r'^book_tour/(?P<id>\d+)$', views.book_tour,name='book_tour'),
	url(r'^add_review/(?P<id>\d+)$', views.add_review,name='add_review'),
	path('user_view_booking', views.user_view_booking,name='user_view_booking'),
	path('view_blog', views.view_blog,name='view_blog'),
	path('add_blog', views.add_blog,name='add_blog'),
	path('user_search_package', views.user_search_package,name='user_search_package'),

	url(r'^details_hospital/(?P<id>\d+)$', views.details_hospital,name='details_hospital'),
	url(r'^details_hotels/(?P<id>\d+)$', views.details_hotels,name='details_hotels'),
	url(r'^details_medical/(?P<id>\d+)$', views.details_medical,name='details_medical'),
	url(r'^details_petrol/(?P<id>\d+)$', views.details_petrol,name='details_petrol'),
	url(r'^details_cab/(?P<id>\d+)$', views.details_cab,name='details_cab'),
	url(r'^details_railway/(?P<id>\d+)$', views.details_railway,name='details_railway'),
	url(r'^details_bus/(?P<id>\d+)$', views.details_bus,name='details_bus'),

	url(r'^book_hotel/(?P<id>\d+)$', views.book_hotel,name='book_hotel'),
	url(r'^book_cab/(?P<id>\d+)$', views.book_cab,name='book_cab'),
	url(r'^save_hotel_book/(?P<id>\d+)$', views.save_hotel_book,name='save_hotel_book'),
	url(r'^save_cab_book/(?P<id>\d+)$', views.save_cab_book,name='save_cab_book'),

	url(r'^add_rating_hotel/(?P<id>\d+)$', views.add_rating_hotel,name='add_rating_hotel'),
	url(r'^add_rating_cab/(?P<id>\d+)$', views.add_rating_cab,name='add_rating_cab'),

	url(r'^delete_package/(?P<id>\d+)$', views.delete_package,name='delete_package'),	
	url(r'^delete_user/(?P<id>\d+)$', views.delete_user,name='delete_user'),	

	url(r'^edit_hotel/(?P<id>\d+)$', views.edit_hotel,name='edit_hotel'),	
	url(r'^update_hotel/(?P<id>\d+)$', views.update_hotel,name='update_hotel'),
	url(r'^delete_hotel/(?P<id>\d+)$', views.delete_hotel,name='delete_hotel'),
	url(r'^edit_bustand/(?P<id>\d+)$', views.edit_bustand,name='edit_bustand'),
	url(r'^update_bustand/(?P<id>\d+)$', views.update_bustand,name='update_bustand'),
	url(r'^delete_bus/(?P<id>\d+)$', views.delete_bus,name='delete_bus'),
	url(r'^edit_cab/(?P<id>\d+)$', views.edit_cab,name='edit_cab'),
	url(r'^update_cab/(?P<id>\d+)$', views.update_cab,name='update_cab'),
	url(r'^delete_cab/(?P<id>\d+)$', views.delete_cab,name='delete_cab'),
	url(r'^edit_hospital/(?P<id>\d+)$', views.edit_hospital,name='edit_hospital'),
	url(r'^update_hospital/(?P<id>\d+)$', views.update_hospital,name='update_hospital'),
	url(r'^delete_hospital/(?P<id>\d+)$', views.delete_hospital,name='delete_hospital'),
	url(r'^edit_petrol/(?P<id>\d+)$', views.edit_petrol,name='edit_petrol'),
	url(r'^update_petrol/(?P<id>\d+)$', views.update_petrol,name='update_petrol'),
	url(r'^delete_petrol/(?P<id>\d+)$', views.delete_petrol,name='delete_petrol'),
	url(r'^edit_medical/(?P<id>\d+)$', views.edit_medical,name='edit_medical'),
	url(r'^update_medical/(?P<id>\d+)$', views.update_medical,name='update_medical'),
	url(r'^delete_medical(?P<id>\d+)$', views.delete_medical,name='delete_medical'),
	url(r'^edit_railway(?P<id>\d+)$', views.edit_railway,name='edit_railway'),
	url(r'^update_railway(?P<id>\d+)$', views.update_railway,name='update_railway'),
	url(r'^delete_railway(?P<id>\d+)$', views.delete_railway,name='delete_railway'),	

	path('rate_app', views.rate_app,name='rate_app'),
	path('submit_rating', views.submit_rating,name='submit_rating'),

	path('store_management', views.store_management,name='store_management'),
	path('coupon_list', views.coupon_list,name='coupon_list'),

]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)  