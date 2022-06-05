from unicodedata import name
from django.urls import path 
from .import views



urlpatterns = [
    path('',views.main_page,name="main"),
    path('job-d/<int:pk>',views.job_details, name='job_d'),
    path('elements/', views.element_page, name="element_s"),
    path('single-b/', views.single_blog, name="single_b"),
    path('job-l/', views.job_list, name="job_l"),
    path('contact/', views.contact_page, name="contact_p"),
    path('about/', views.about_page, name="about_p"),
    path('blog/', views.blog_page, name="blog_p"),
    path('regis/', views.register_page, name="regis_p"),
    path('login/', views.login_page, name="login"),
    path('creat_ad/', views.login_page, name="creat"),
    path('test/',views.test1,name="test"),
]

