from django.urls import path
from .import views


urlpatterns = [

    path('todo/',views.todo),
    path('FormHandle/',views.FormHandle),
    path('updatetask/',views.updatetask),
    path('deletetask/',views.deletetask),
    path('seealltask/',views.seealltask)



]