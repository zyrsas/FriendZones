from django.conf.urls import url
from django.contrib import admin
from friendsZones import views
from django.conf.urls.static import static
from FriendZones.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sing_in/$', views.SignIn),
    url(r'^favorites/$', views.AddRemoveFavorites),
    url(r'^all_favorites/$', views.GetAllFavorites),
    url(r'^update_user/$', views.UpdateUser),
    url(r'^block/$', views.AddRemoveBlock),
    url(r'^push/$', views.SendPushNotification),
    url(r'^inradius/$', views.inRadius),
    url(r'^upload/$', views.uploadPickture),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
