from django.conf.urls.defaults import *

urlpatterns = patterns('randallo.views',
    # GUI
    (r'^/?$', 'index'),
    
    # API
    (r'^api/getrandomepisode/?$', 'get_random_episode'),
    (r'^api/getrandomunwatchedepisode/?$', 'get_random_unwatched_episode'),
    (r'^api/getepisode/(?P<episode_no>\d{1,2})/?$', 'get_episode'),
    (r'^api/watchepisode/(?P<episode_no>\d{1,2})/?$', 'watch_episode'),
    (r'^api/getviewinghistory', 'get_viewing_history'),
    (r'^api/clearviewinghistory/?$', 'clear_viewing_history'),
)
