import gettext  # A gettext modul importálása nemzetközi fordításhoz (i18n).
from jinja2 import Environment, FileSystemLoader  # Jinja2 importálása sablon rendereléshez.

# A fordításokhoz tartozó domain neve (messages.po/messages.mo fájlok neve).
domain = 'messages'

# A kiválasztott nyelvi környezet: angol (Egyesült Államok).
current_locale = 'en_US'

# A lokalizációs fájlokat tartalmazó könyvtár elérési útja.
locale_path = 'locales/'

# GNU gettext fordítás betöltése a megadott domain és nyelv alapján.
gnu_translations = gettext.translation(
    domain=domain,         # Fordítási domain neve.
    localedir=locale_path, # A fordítási fájlokat tartalmazó könyvtár.
    languages=[current_locale]  # Használni kívánt nyelv(ek) listája.
)

# MEGJEGYZÉS: A következő két sort kikommentezted, mert lehet, hogy nincs rá szükség.
# Ha ezek aktívak, akkor a `_` függvény globálisan elérhetővé válik a fordításokhoz.

# gnu_translations.install()  # A `_` fordító függvény globális elérhetővé tétele.
# _ = gettext.gettext  # `_`-ként aliasolva a fordító függvény.

# Jinja2 környezet létrehozása a sablonok rendereléséhez.
env = Environment(
    loader=FileSystemLoader('templates'),  # A sablonokat tartalmazó könyvtár megadása.
    extensions=['jinja2.ext.i18n']         # Az i18n kiterjesztés engedélyezése fordításokhoz.
)

# A gettext fordítások összekapcsolása a Jinja2 környezettel.
env.install_gettext_translations(gnu_translations, newstyle=True)

# Például használt adatok:
ids = {
    'items': 'Yes'
}
student = {
    'full_name': 'John Doe',
    'ids': ids
}

# A sablon betöltése a megadott könyvtárból
template = env.get_template('index.html')

# A sablon renderelése
result = template.render(student=student)

# A renderelt sablon kiírása a konzolra.
print(result)

output_file = 'templates/English.html'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(result)

# Mi történik pontosan
# Belenyúlni a programba (extract)
# ID-k

# Babel extract
# pybabel extract --mapping babel.cfg --output-file=locales/messages.pot .
#--mapping-file=MAPPING_FILE, --mapping=MAPPING_FILE path to the mapping configuration file
#--output-file=OUTPUT_FILE, --output=OUTPUT_FILE name of the output file
