import gettext
from jinja2 import Environment, FileSystemLoader

# Fordítás betöltése angol nyelvhez (en)
translations = gettext.translation('messages', localedir='locales', languages=['en'])
translations.install()
_ = translations.gettext

# Jinja2 környezet létrehozása és fordítás hozzáadása
env = Environment(
    loader=FileSystemLoader('templates'),
    extensions=['jinja2.ext.i18n']
)
env.install_gettext_translations(translations)

template = env.get_template('index.html.j2')
print(template.render())

