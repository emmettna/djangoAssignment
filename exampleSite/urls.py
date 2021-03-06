"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from assignment.views import user_profile, match_list, user_rank, bet_list, player_list, bet_history


# url(r'^user_profile/(?P<usn>\w{0,50})/$', user_profile)
# Takes parameter in URL sending to user_profile Function

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user_profile/$', user_profile),
    url(r'^user_profile/(?P<usn>\w{0,50})/$', user_profile),
    url(r'^match_list/(?P<usn>\w{0,50})/$', match_list),
    url(r'^user_rank/(?P<usn>\w{0,50})/$', user_rank),
    url(r'^bet_list/(?P<usn>\w{0,50})/$', bet_list),
    url(r'^player_list/(?P<team_id>\w{0,50})/$', player_list),
    url(r'^bet_history/(?P<usn>\w{0,50})/$', bet_history),
]
