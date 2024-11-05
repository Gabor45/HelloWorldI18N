import gettext
from jinja2 import Environment, FileSystemLoader

domain = 'messages'
current_locale = 'en_US'
locale_path = 'locales/'

# Fordítás betöltése angol nyelvhez (en)
gnu_translations = gettext.translation(
    domain=domain,
    localedir=locale_path,
    languages=[current_locale]
)
gnu_translations.install()  # Magically make the _ function globally available
_ = gettext.gettext

# Jinja2 környezet létrehozása és fordítás hozzáadása
env = Environment(
    loader=FileSystemLoader('templates'),
    extensions=['jinja2.ext.i18n']
)
env.install_gettext_translations(gnu_translations, newstyle=True)

template = env.get_template('index.jinja2')
result = template.render()
print(result)

# Mi történik pontosan
# Belenyúlni a programba (extract)
# ID-k

