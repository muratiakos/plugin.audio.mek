# MEK - Audibooklibrary plugin for Kodi


## Development
The project uses `KodiSwift`:
 - https://github.com/afrase/kodiswift/blob/master/docs/quickstart.rst 


### Setup your virtualenv for Python
Follow notes from:
 - https://virtualenvwrapper.readthedocs.io/en/latest/install.html
```bash
# Install your Python virtualenv
pip install virtualenv
pip install virtualenvwrapper

# Setup your virtualenv for kodiswift
mkvirtualenv kodiswift
workon kodiswift
pip install kodiswift
deactivate
```

### Run the plugin in the CLI
```bash
kodiswift run
kodiswift run interactive
```
