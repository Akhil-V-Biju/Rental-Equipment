from django.urls import path
from.import views


urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    # path('add_profile',views.add_profile,name='add_profile'),
    path('add_pro',views.add_pro,name='add_pro'),
    path('profile',views.profile,name='profile'),
    path('update_profile/<int:pk>/',views.update_profile,name='update_profile'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admin_panel',views.admin_panel,name='admin_panel'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
    path('add_equipment', views.add_equipment, name='add_equipment'),
    path('view_equipment',views.view_equipment,name='view_equipment'),
    path('del_st/<int:pk>/',views.del_st,name='del_st'),
    path('view_cart/<int:pk>/',views.view_cart,name='view_cart'),
    path('buy_cart/<int:pk>/',views.buy_cart,name='buy_cart'),
    path('history',views.history,name='history'),
    path('approve_requst/<int:pk>/',views.approve_requst,name='approve_requst'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('update_equipment/<int:pk>/',views.update_equipment,name='update_equipment'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('testi',views.testi,name='testi'),

]