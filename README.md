# Setup

```bash
[sudo] pip install -r requirements.txt
```

## Compile `po` files

The `po` files (human readable) need to be compiled into machine readable `mo` files before gettext can use them

```bash
pybabel compile --domain=messages --directory=locales --use-fuzzy
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
