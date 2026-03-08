## zadanie:

w systemie do rejestracji sal dodal i18n.

Niech choc pare tekstow zmienia sie przy zmiane wersji jezykowej

1. urls.py - dodajemy url zwiazane z i18n
2. settings.py - dodajemy wymagane do dzialania i18n + LocaleMiddleware
3. w szablonach dodajemy {% load i18n %} i potem mamy  {% trans "text" %} lub {% blocktrans %}text{% endblocktrans %}
4. dodajemy przelacznik w szablonie glownym