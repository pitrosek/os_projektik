# Flask Shop Example

Instrukce pro nastavení a běh projektu.

1. Vytvořte virtuální prostředí (pokud ještě není):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Nastavte proměnné prostředí (volitelně):

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
export DATABASE_URL=sqlite:///app.db
```

3. Inicializace databáze (Flask-Migrate / Alembic):

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

Dodatečné CLI příkazy:
- `flask db export` — vypíše JSON produktů
- `flask db import <file>` — naimportuje produkty ze souboru
