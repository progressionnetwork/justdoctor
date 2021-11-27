from .core import app as atom
from .view import index, search

atom.register_blueprint(index)
atom.register_blueprint(search)
