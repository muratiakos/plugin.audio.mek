# Readme: https://kodi.wiki/view/Audio/Video_plugin_tutorial
# https://xbmcswift2.readthedocs.io/en/latest/index.html


import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://localhost/some_video.mkv'
li = xbmcgui.ListItem('My First Video!', iconImage='DefaultVideo.png')
li = xbmcgui.ListItem(label='My video')
#li.setIconImage('icon.png')
#li.setArt({'thumb': 'thumbnail.jpg', 'poster': 'poster.jpg' 'fanart': 'fanart.jpg'})

#info = {
#    'genre': 'Horror',
#    'year': 1979,
#    'title': 'Alien',
#}

li.setInfo('video', info)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
