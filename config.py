import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/blog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'app.db')
