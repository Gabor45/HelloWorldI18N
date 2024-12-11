# Basic i18n Guide

This guide provides an initial overview for internationalizing (i18n) a Python application. The goal of i18n is to enable the application to support multiple languages, making it accessible to users speaking different languages.

## 1. Prerequisites

To ensure everything works correctly, install the following:
```bash
[sudo] pip install Babel
[sudo] pip install jinja2
```

---

## 2. Creating the `locales` Directory

The directory structure for storing translations should follow this pattern:

```
locales/
├── en_US/
│   └── LC_MESSAGES/
│       ├── messages.po
│       └── messages.mo
├── hu_HU/
│   └── LC_MESSAGES/
│       ├── messages.po
│       └── messages.mo
```

- **`locales`**: The main folder for storing translation files.
- **`en_US`**: Folder for English translations.
- **`LC_MESSAGES`**: Subfolder containing `.po` (text) and `.mo` (binary) translation files.

---

## 3. Using `.po` Files for Translation

In a `.po` file, specify how the gettext function should translate each string:
```po
msgid "Hiányzó adatok."
msgstr "Missing data."
```

---

## 4. Converting `.po` Files to `.mo` Files

To make these translations work, the `.po` files must be converted into `.mo` files.

For this, use the Pybabel `compile` method.

Run the following command in the terminal, ensuring Babel is installed:
```bash
pybabel compile --domain=messages --directory=locales --use-fuzzy
```

- `--domain=messages`: Specifies the name of the `.po` file.
- `--directory=locales`: Specifies the path to the main directory.
- `--use-fuzzy`: Includes fuzzy translations.

---

## 5. Jinja2 és Python fileokhoz gettext hozzáadása

### 5.1 Jinja2

```
Ez a szekció mutatja a csapatokat, amelyeknek {{ student.full_name }} tagja.
```

```
{{ gettext('Ez a szekció mutatja a csapatokat, amelyeknek %(student.full_name)s tagja.')
% { 'student.full_name' : student.full_name }
```

### 5.2 Python

```
description=f"{source_name} elem kapcsolódik {target_name} elemhez."
```

```
description=gettext("%(source_name)s elem kapcsolódik %(target_name)s elemhez.")
% {'source_name':source_name, 'target_name':target_name}
```
Ilyet még lehet, de viszont ha hozzáadunk így hozzá akkor a következő stringnél space-t kell nyomni, mert akkor egybe veszi a po-fileban pl: ```msgid "Elem kapcsolódik"```

```
description=gettext('Elem'+' kapcsolódik')
```

Ha pedig space nélkül adjuk meg : ```msgid "Elemkapcsolódik"```

```
description=gettext('Elem'+'kapcsolódik')
```

Ilyet pedig nem lehet mert nem ismeri fel a változó értékét: ``` msgid "Elemkapcsolódik" ```

```
string="ehhez a tárgyhoz"
description=gettext('Elem'+'kapcsolódik'+string)
```


# Run

```bash
python main.py
```

# Workflow

When working on the application, you might want to add new messages. For example, add the following line to `templates/index.jinja2`:

```jinja2
{{ gettext('Yet another message') }}
```

Babel can automatically detect that this message was added. First we need to use the `extract` command to extract all localizable messages from the source files:

```bash
pybabel extract --mapping babel.cfg --output-file=locales/messages.pot .
```

Then update the *.po files so they contain the new localizable message:

```bash
pybabel update --domain=messages --input-file=locales/messages.pot --output-dir=locales
```

You can now see in the git diff for the *.po files where the new message was added, and you can hand-edit these files to localize the new message.

For example, open `locales/en_US/LC_MESSAGES/messages.po` and edit
```pot
#: templates/index.jinja2:2
msgid "language"
msgstr ""

#: templates/index.jinja2:6
msgid "title"
msgstr ""

#: templates/index.jinja2:9
msgid "Hello Világ"
msgstr ""
```
to
```pot
#: templates/index.jinja2:2
msgid "language"
msgstr "en"

#: templates/index.jinja2:6
msgid "title"
msgstr "Welcome"

#: templates/index.jinja2:9
msgid "Hello Világ"
msgstr "Hello World"
```

[Poedit](https://poedit.net/) is a good editor for doing this. For example, it'll highlight missing translations and suggest translations, and you'll just have to press a keyboard shortcut to apply the suggestion.

## Command line aliases

Since the `pybabel` commands can be quite long, and you might want to use them frequently, it is recommended to add short aliases to these commands to save time
