import logging
import os
from pathlib import Path

from flask import Flask

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -    %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)

app = Flask(
    __name__,
    template_folder='build',
    static_folder='build',
    root_path=Path(os.getcwd()) / 'justatom',
)

