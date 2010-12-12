# TODO accented characters
# TODO check names of episodes
# TODO upload to github
# TODO put online
# TODO check and comment

import logging
import simplejson as json

from randallo.engine import alloallo
from django import http, shortcuts

COOKIE_KEY = 'recently_watched'
COOKIE_PATH = '/'
COOKIE_MAX_AGE = 31536000 # 1 year in seconds

# GUI

def index(request):
    """The random 'Allo 'Allo episode page"""
    return shortcuts.render_to_response(u'randallo/index.html')

# API

def get_random_episode(request):
    """Get a random 'Allo 'Allo episode."""
    show = alloallo.get_show()
    
    episode = show.get_random_episode()
    
    response_dict = {}
    
    if episode != None:
        response_dict[u'episode'] = __make_episode_dict(episode)
    
    return http.HttpResponse(json.dumps(response_dict, separators=(u',',u':')), mimetype=u'application/json')

def get_random_unwatched_episode(request):
    """Get a random 'Allo 'Allo episode which hasn't been watched recently.
    The recently watched episode numbers are stored in a cookie."""
    
    # Get the recently watched episodes from the cookie
    recently_watched = []
    
    if COOKIE_KEY in request.COOKIES:
        recently_watched = request.COOKIES[COOKIE_KEY].split(':')
    
    show = alloallo.get_show()
    
    # Convert the recently watched episode cookie to a list of Episodes
    recently_watched_episode_list = []
    
    for recent_episode_no in recently_watched:
        try:
            recently_watched_episode = show.get_episode(int(recent_episode_no))
            recently_watched_episode_list.append(recently_watched_episode)
        except ValueError:
            None
    
    episode = show.get_random_episode(episode_ignore_list=recently_watched_episode_list)
    
    response_dict = {}
    
    if episode != None:
        response_dict[u'episode'] = __make_episode_dict(episode)
    
    return http.HttpResponse(json.dumps(response_dict, separators=(u',',u':')), mimetype=u'application/json')

def get_episode(request, episode_no):
    """Get an episode for a given episode number."""
    i_episode_no = 0
    
    try:
        i_episode_no = int(episode_no)
    except ValueError:
        raise http.Http404
    
    show = alloallo.get_show()
    episode = show.get_episode(i_episode_no)
    
    if episode == None:
        raise http.Http404

    response_dict = {}
    response_dict[u'episode'] = __make_episode_dict(episode)
    
    return http.HttpResponse(json.dumps(response_dict, separators=(u',',u':')), mimetype=u'application/json')

def watch_episode(request, episode_no):
    """Add the specified episode number to the list of watched episodes in the
    client cookie."""
    
    i_episode_no = 0
    
    try:
        i_episode_no = int(episode_no)
    except ValueError:
        raise http.Http404
    
    # Get the episode we are to record as watched
    show = alloallo.get_show()
    episode = show.get_episode(i_episode_no)
    
    if episode == None:
        raise http.Http404

    # Get the current cookie value
    recently_watched = []
    
    if COOKIE_KEY in request.COOKIES:
        recently_watched = request.COOKIES[COOKIE_KEY].split(':')
    
    # Make the new list of watched episodes cookie
    # First add the new episode, and then add all the others, excluding any other
    # instance of this one so every episode can only exist in the list once
    new_recently_watched = []
    new_recently_watched.append(i_episode_no)
    
    for recent_episode_no in recently_watched:
        try:
            i_recent_episode_no = int(recent_episode_no)
            
            if i_recent_episode_no != i_episode_no:
                new_recently_watched.append(i_recent_episode_no)
                
        except ValueError:
            None
    
    # Convert the list to a string
    new_recently_watched_str = ''
    for recent_episode_no in new_recently_watched:
        if len(new_recently_watched_str) > 0:
            new_recently_watched_str += ':'
        new_recently_watched_str += str(recent_episode_no)
    
    response = http.HttpResponse(json.dumps([], separators=(u',',u':')), mimetype=u'application/json')
    response.set_cookie(key=COOKIE_KEY, value=new_recently_watched_str, max_age=COOKIE_MAX_AGE, path=COOKIE_PATH)
    
    return response

def get_viewing_history(request):
    """Get the details of all the episodes the user has watched recently."""
    
    # Get the recently watched episodes from the cookie
    recently_watched = []
    
    if COOKIE_KEY in request.COOKIES:
        recently_watched = request.COOKIES[COOKIE_KEY].split(':')

    show = alloallo.get_show()
    
    episode_list = []
    
    for episode_no in recently_watched:
        try:
            episode = show.get_episode(int(episode_no))
    
            if episode != None:
                episode_list.append(__make_episode_dict(episode))
        except ValueError:
            None

    response_dict = {}
    response_dict['episode_list'] = episode_list
    
    return http.HttpResponse(json.dumps(response_dict, separators=(u',',u':')), mimetype=u'application/json')

def clear_viewing_history(request):
    """Clear the user's list of recently watched episodes by removing the
    cookie."""
    response = http.HttpResponse(json.dumps([], separators=(u',',u':')), mimetype=u'application/json')
    response.delete_cookie(COOKIE_KEY)
    
    return response

def __make_series_dict(series):
    """Make a dictionary of a Series object for returning as JSON."""
    series_dict = None
    
    if series != None:
        series_dict = {
            u'name': series.name,
            u'url': series.url,
        }
        
    return series_dict
    
def __make_episode_dict(episode):
    """Make a dictionary of a Episode object for returning as JSON."""
    episode_dict = None
    
    if episode != None:
        episode_dict = {
            u'episode_no': episode.episode_no(),
            u'series_episode_no': episode.series_episode_no(),
            u'name': episode.name,
            u'url': episode.url,
            u'series': __make_series_dict(episode.series),
        }
        
    return episode_dict
