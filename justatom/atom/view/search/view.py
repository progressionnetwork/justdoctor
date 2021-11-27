from flask import Blueprint
from pathlib import Path
import os


search = Blueprint(
    'search',
    __name__,
    template_folder='build',
    static_folder='build',
    root_path=Path(os.getcwd()) / 'justatom'
)
