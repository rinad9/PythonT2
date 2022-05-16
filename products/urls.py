# to reference a url we have to import the path function
# . means current folder
from django.urls import path
from . import views

#  in this list we map various urls to thier view functions
urlpatterns = [
# the first argument is the root of the app 
# like when we say \index or somthin
# the second argument is the view finction from function in view
# we dont call the function we just reference it 
# django will take care of the calling when the request comes
    path('', views.index),
    path('new', views.new)

]