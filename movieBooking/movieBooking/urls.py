"""
URL configuration for movieBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',views.adminLogin),
    path('adminList/',views.adminList),
    path('addLocation/',views.addLocation),
    path('addTheatre/',views.addTheatre),
    path('addMovies/',views.addMovies),
    path('addPremiere/',views.addPremiere),
    path('addEvents/',views.addEvents),
    path('addCast/',views.addCast),
    path('addPoster/',views.addAdds),
    path('locationManage/',views.locationManage),
    path('deletelocation/<int:id>/',views.deleteLocation),
    path('editlocation/<int:id>/',views.editLocation),
    path('theatreManage/',views.theatreManage),
    path('deletetheatre/<int:id>/',views.deleteTheatre),
    path('edittheatre/<int:id>/',views.editTheatre),
    path('userManage/',views.userManage),
    path('movieManage/',views.movieManage),
    path('deletemovie/<int:id>/',views.deleteMovie),
    path('editmovie/<int:id>/',views.editMovie),
    path('premiereManage/',views.premiereManage),
    path('deletepremiere/<int:id>/',views.deletePremiere),
    path('editpremiere/<int:id>/',views.editPremiere),
    path('eventManage/',views.eventManage),
    path('deleteevent/<int:id>/',views.deleteEvent),
    path('editevent/<int:id>/',views.editEvent),
    path('paymemtManage/',views.paymentManage),
    path('castManage/',views.castManage),
    path('deletecast/<int:id>/',views.deleteCast),
    path('editcast/<int:id>/',views.editCast),
    path('posterManage/',views.addManage),
    path('deleteposter/<int:id>/',views.deleteAdd),
    path('editposter/<int:id>/',views.editAdd),

    path('userHome/',views.userHomePage),
    path('signup/',views.signUp),
    path('login/',views.signIn),
    path("movieinner/<int:id>/",views.movieInner),
    path("premiereinner/<int:id>/",views.premiereInner),
    path("eventinner/<int:id>/",views.eventInner),
    path('payment/<int:id>/',views.Payment)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
