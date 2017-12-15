# manage.py

import unittest
from flask_script import Manager

from project import create_app, db
from project.api.models import User
from flask_migrate import MigrateCommand

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(
        username='michael',
        email='michael@realpython.com',
        password='test'
    ))
    db.session.add(User(
        username='michaelherman',
        email='michael@mherman.org',
        password='test'
    ))
    db.session.commit()


if __name__ == '__main__':
    manager.run()
