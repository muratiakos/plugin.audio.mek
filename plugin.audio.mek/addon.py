# -*- coding: utf-8 -*-
from kodiswift import Plugin

# https://kodi.wiki/view/Add-on:Parsedom_for_xbmc_plugins

plugin = Plugin()

@plugin.route('/')
def index():
    items = [
        {'label': 'Hola Kodi!', 'path': plugin.url_for('show_label', label='spanish')},
        {'label': 'Bonjour Kodi!', 'path': plugin.url_for('show_label', label='french')},
    ]
    return items


@plugin.route('/labels/<label>/')
def show_label(label):
    # Normally we would use label to parse a specific web page, in this case we are just
    # using it for a new list item label to show how URL parsing works.
    items = [
        {'label': label},
    ]
    return items


if __name__ == '__main__':
    plugin.run()
