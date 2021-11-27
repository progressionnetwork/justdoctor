import ast
import itertools
import json
import pathlib
from typing import Union

import numpy as np

from justatom.ir.document_store import base


def get_batches_from_generator(iterable, n):
    """
    Batch elements of an iterable into fixed-length chunks or blocks.
    """
    it = iter(iterable)
    x = tuple(itertools.islice(it, n))
    while x:
        yield x
        x = tuple(itertools.islice(it, n))


def chunked_dict(dictionary, size):
    it = iter(dictionary)
    for i in range(0, len(dictionary), size):
        yield {k: dictionary[k] for k in itertools.islice(it, size)}


def load(
    data_dir: Union[pathlib.Path, str], filename: str, embedding_field="embedding", ext=".json"
):
    data_dir = pathlib.Path(data_dir)
    db_filename = filename
    db_filepath = data_dir / (db_filename + ext)

    with open(str(db_filepath), "r", encoding="utf-8") as j_ptr:
        docs = json.load(j_ptr)

    for d in docs:
        if "meta" in d.keys():
            try:
                d["meta"] = ast.literal_eval(d["meta"])
            except ValueError as e:
                continue

    if embedding_field is not None:
        index_filename = filename + "_index" + ".npy"
        index_filepath = data_dir / index_filename
        embeddings = np.load(str(index_filepath))
        for iDoc, iEmb in zip(docs, embeddings):
            iDoc[embedding_field] = iEmb

    return docs
