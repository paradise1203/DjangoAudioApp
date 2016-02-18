from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'dvach.views.show_dvach', name='show_dvach'),
    url(r'^post/(?P<post_id>\d+)', 'dvach.views.comment', name='comment')
]
