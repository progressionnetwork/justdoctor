from .view import index
from flask import send_from_directory
import os

@index.route('/', defaults={'path': ''})
@index.route("/<path:path>")
def atom_index(path):
    if path != '' and os.path.exists(index.static_folder + '/' + path):
        return send_from_directory(index.static_folder, path)
    else:
        return send_from_directory(index.static_folder, 'index.html')
