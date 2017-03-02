from django.conf.urls import url
from . import views

urlpatterns = [
    # 문자열이 아무것도 없는 경우 매칭
    url(r'^$', views.post_list, name='post_list'),
]
