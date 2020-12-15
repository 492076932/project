from django.urls import path

from update import views

urlpatterns = [
    path('update_doc',views.update_doc),
    path('all_doc',views.all_doc),
    path('delete_doc',views.delete_doc),
    path('schedule',views.schedule),
    path('add_doc',views.add_doc),
]