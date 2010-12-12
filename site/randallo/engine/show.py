"""Classes to represent a TV Show, a Series within that Show and an Episode in a Series.
Episodes may also be standalone and not in a Series."""

import random

class Series:
    """A TV Series."""
    
    def __init__(self, name, url=None, episodes=[], show=None):
        """episodes is a list of Episodes in the order they appear in the Series.
        show can be left to be set automatically when the Series is passed to
        the constructor of a Show object."""
        self.name = name
        self.url = url
        self.episodes = episodes
        self.show = show
        
        # Put reference to the series on each episode
        for episode in self.episodes:
            episode.series = self
            episode.show = self.show

    def __str__(self):
        return str(self.name)
    
    def __unicode__(self):
        return unicode(self.name)

class Episode:
    """An Episode of a TV Series, or a standalone episode such as a Pilot."""
    
    def __init__(self, name, url=None, series=None, show=None):
        """series can be left to be set automatically when the Episode is passed
        to the constructor of a Series object, and likewise show can be left to
        be set automatically when the Episode (or its Series) is passed to the
        constructor of a Show object."""
        self.name = name
        self.url = url
        self.series = series
        self.show = show

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return unicode(self.name)
        
    def series_episode_no(self):
        """Return the episode number within the Series the episode is part of.
        Returns None if the Episode is not part of a Series."""
        no = None
        
        if self.series != None:
            no = self.series.episodes.index(self) + 1
        
        return no
    
    def episode_no(self):
        """Return the episode number within the entire Show the episode is part
        of. Returns None if the Episode is not part of a Show."""
        no = None

        if self.show != None:
            no = self.show.all_episodes.index(self) + 1
            
        return no
    
class Show:
    """A TV Show."""
    
    def __init__(self, name, url=None, content=[]):
        """content is a list of Series' and standalone Episodes in the order they
        appear in the run of the Show."""
        self.name = name
        self.url = url
        self.content = content
        
        # Make lists of all Episodes and all Series and add a reference to this
        # Show to each one.
        self.all_episodes = []
        self.all_series = []
        
        for c in content:
            if c.__class__ == Episode:
                self.all_episodes.append(c)
                c.show = self
            elif c.__class__ == Series:
                self.all_series.append(c)
                c.show = self
                
                for e in c.episodes:
                    self.all_episodes.append(e)
                    e.show = self
        
    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return unicode(self.name)

    def get_episode(self, episode_no):
        """Get a specific Episode of this Show. episode_no starts at 1."""
        episode = None

        if episode_no - 1 < len(self.all_episodes):
            episode = self.all_episodes[episode_no - 1]
    
        return episode

    def get_random_episode(self, episode_ignore_list=None):
        """Get a random episode of this Show. If episode_ignore_list is not None
        then any Episodes in the list are left out of the ones randomly selected
        from. If all episodes are in the ignore list then returns None."""
        
        # Make the list of episodes to randomly select from
        episode_list = self.__filter_episodes(episode_ignore_list)
        
        random_episode = None
    
        if len(episode_list) > 0:
            rand_episode_no = random.randint(0, len(episode_list) - 1)
    
            random_episode = episode_list[rand_episode_no]
    
        return random_episode

    def __filter_episodes(self, episode_ignore_list):
        """Return a list of all episodes in the Show except any contained in the
        episode_ignore_list."""
        episode_list = list(self.all_episodes)
        
        if episode_ignore_list != None:
            for episode in episode_ignore_list:
                episode_list.remove(episode)
        
        return episode_list

    def episode_count(self):
        """Return the total number of episodes in this Show."""
        return len(self.all_episodes)
