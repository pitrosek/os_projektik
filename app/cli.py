import click
from flask import current_app
from flask.cli import with_appcontext
from . import db
from .models import Product
import json


def register(app):
    # If Flask-Migrate already registered a 'db' group, extend it; otherwise create one.
    existing = app.cli.commands.get('db')

    if existing is None:
        @app.cli.group(name='db')
        def db():
            """Database related commands (extended)"""
            pass
    else:
        db = existing

    # Define export and import as plain functions, then add to the group.
    @click.command('export')
    @with_appcontext
    def export():
        products = Product.query.all()
        data = [p.to_dict() for p in products]
        click.echo(json.dumps(data, indent=2))

    @click.command('import')
    @click.argument('file')
    @with_appcontext
    def import_(file):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            p = Product(name=item['name'], description=item.get('description'), price=item.get('price', 0))
            db.session.add(p)
        db.session.commit()
        click.echo('Imported')

    try:
        # add_command exists on click Group
        db.add_command(export)
        db.add_command(import_)
    except Exception:
        # fallback: register directly on app CLI with prefixed names
        app.cli.add_command(export, name='db-export')
        app.cli.add_command(import_, name='db-import')
