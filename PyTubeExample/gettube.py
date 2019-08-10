import os
import re
import django

from pytube import YouTube

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_name.settings")
django.setup()

from core.models import User
from app_name import settings


if __name__ == '__main__':
	""" Script for dowloading youtube videos in django projects.
	
	In download you can select wide range of options (line: 31, 34):
		- resolution
		- quality
		- extension
		- download path
		- download title
		- ...
		
		and more other.
		
	Using PuTube : https://github.com/nficano/pytube/blob/master/docs/index.rst
	version: 9.5.1
	
	P.S: in this moment (10.08.2019) lib has some bugs, but in issures contains all fixes. 
	
	"""
    SAVE_PATH = settings.MEDIA_ROOT + '/videos/'

    if not user.video_low_q and not user.video_high_q:
        LOAD_LINK = '<VIDEO_URL>'
        yt = YouTube(LOAD_LINK)
        regex = re.compile('[^a-zA-Zа-яА-Я0-9 ]')
        title = title.replace(' ', '_')
        title = regex.sub('', yt.title)

        print('Download \'' + title + '\' in 480p quality...')
        yt.streams.filter(res='480p', file_extension='mp4').first().download(SAVE_PATH, title + '-480p')
        user.video_low_q = 'videos/' + title + '-480p.mp4'

        print('Download \'' + title + '\' in 720p quality...')
        yt.streams.filter(res='720p', file_extension='mp4').first().download(SAVE_PATH, title + '-720p')
         user.video_high_q = 'videos/' + title + '-720p.mp4'

        lesson.save()
