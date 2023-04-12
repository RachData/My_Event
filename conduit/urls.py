
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(('conduit.apps.articles.urls', 'articles'), namespace='articles')),
    path('api/', include(('conduit.apps.authentication.urls', 'authentication'), namespace='authentication')),
    path('api/', include(('conduit.apps.profiles.urls', 'profiles'), namespace='profiles')),
    path('api/', include(('conduit.apps.events.urls', 'events'), namespace='events')),
]
