from django.urls import path,include
from . views import *

urlpatterns = [
    path('homepage/',home,name="home"),
    # path('student_data/',studentdata,name='student data'),
    # path('create_studentdata/',post_student,name="create_student"),
    # path('update_student/<int:pk>/',update_student,name="update_student"),
    # path('delete_student/<int:id>/',delete_student,name="delete_student"),
    path('books/',get_book,name="list_books"),
    path('student_list/',StudentAPI.as_view(),name='student_api'),
    path('student_list/<int:id>/',StudentAPI.as_view(),name='student_api'),
    path('register/',Registration.as_view(),name='register_user'),
    path('student_generic/',StudentGeneric.as_view(),name='student_generic_view'),
    path('student_generic/<id>/',StudentGeneric1.as_view(),name='generic_student_view'),
]
