from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('signup', views.signup, name='signup'),
    path('signout',views.signout,name='signout'),

    path('detail',views.detail, name='detail'),
    path('detail2',views.detail2, name='detail2'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile, name='profile'),
    path('dsearch',views.dsearch, name='dsearch'),
    path('edit',views.edit, name='edit'),
    path('didentity',views.didentity, name='didentity'),
    path('dcontact',views.dcontact, name='dcontact'),
    path('donsearch/<str:username>/',views.donsearch, name='donsearch'),
    path('donidentity/<str:username>/',views.donidentity, name='donidentity'),
    path('doncontact/<str:username>/',views.doncontact, name='doncontact'),
    path('donacceptreject/<str:username>/', views.donacceptreject, name='donacceptreject'),

    path('rdetail',views.rdetail, name='rdetail'),
    path('rdetail2',views.rdetail2, name='rdetail2'),
    path('rdashboard',views.rdashboard,name='rdashboard'),
    path('ridentity',views.ridentity, name='ridentity'),
    path('rcontact',views.rcontact, name='rcontact'),
    path('rprofile',views.rprofile, name='rprofile'),
    path('rsearch',views.rsearch, name='rsearch'),
    path('recidentity/<str:username>/',views.recidentity, name='recidentity'),
    path('reccontact/<str:username>/',views.reccontact, name='reccontact'),
    path('recsearch/<str:username>/',views.recsearch, name='recsearch'),
    path('recacceptreject/<str:username>/', views.recacceptreject, name='recacceptreject'),
    path('rnotification',views.rnotification, name='rnotification'),

    
    path('odetail',views.odetail, name='odetail'),
    path('odetail2',views.odetail2, name='odetail2'),
    path('oprofile',views.oprofile, name='oprofile'),
    path('oidentity',views.oidentity, name='oidentity'),
    path('orgidentity/<str:username>/',views.orgidentity, name='orgidentity'),
    path('odashboard',views.odashboard,name='odashboard'),
    path('osearch',views.osearch, name='osearch'),
    path('orgsearch/<str:username>/',views.orgsearch, name='orgsearch'),
    path('orgacceptreject/<str:username>/', views.orgacceptreject, name='orgacceptreject'),

    path('hdetail',views.hdetail, name='hdetail'),
    path('hdetail2',views.hdetail2, name='hdetail2'),
    path('hdashboard',views.hdashboard,name='hdashboard'),
    path('hprofile',views.hprofile, name='hprofile'),
    path('hidentity',views.hidentity, name='hidentity'),
    path('hsearch',views.hsearch, name='hsearch'),
    path('hossearch/<str:username>/',views.hossearch, name='hossearch'),
    path('hosidentity/<str:username>/',views.hosidentity, name='hosidentity'),
    path('hosacceptreject/<str:username>/', views.hosacceptreject, name='hosacceptreject'),


    path('quick',views.quick, name='quick'),
    path('qdon',views.qdon, name='qdon'),
    path('qrec',views.qrec, name='qrec'),
    path('qorg',views.qorg, name='qorg'),
    path('qhos',views.qhos, name='qhos'),
    path('qdashboard',views.qdashboard,name='qdashboard'), 
    
    path('admindash',views.admindash, name='admindash'),
    path('admdonar',views.admdonar, name='admdonar'),
    path('admdonreq',views.admdonreq, name='admdonreq'),
    path('admrecreq',views.admrecreq, name='admrecreq'),
    path('admrec',views.admrec, name='admrec'),
    path('admorg',views.admorg, name='admorg'),
    path('admorgreq',views.admorgreq, name='admorgreq'),
    path('admhos',views.admhos, name='admhos'),
    path('admhosreq',views.admhosreq, name='admhosreq'),
    path('admin_home/',views.admin_home,name="admin_home"),


    path('recreq',views.recreq, name='recreq'),
    path('donreq',views.donreq, name='donreq'),
    path('orgreq',views.orgreq, name='orgreq'),
    path('hosreq',views.orgreq, name='hosreq'),
    ]