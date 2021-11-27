from flask import Blueprint
import os
from pathlib import Path

index = Blueprint(
    'index',
    __name__,
    template_folder='build',
    static_folder='build',
    root_path=Path(os.getcwd()) / 'justatom'
)
