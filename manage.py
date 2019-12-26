import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app.main.routes import add_resources


app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    add_resources(app)
    app.run()

# TODO: Add test


if __name__ == "__main__":
    manager.run()
