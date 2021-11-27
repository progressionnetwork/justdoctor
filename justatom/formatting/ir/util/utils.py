import copy
import logging
from typing import List, Union

import razdel
from justatom.ir.document_store import base
from more_itertools import windowed


def sentinize(text: str) -> List[str]:
    sens = list(razdel.sentinize(text))
    return [_.text for _ in sens]


logger = logging.getLogger(__name__)


def get_unique_docs(
    data: List[Union[dict, base.Document]], field_map: dict
) -> List[base.Document]:
    docs = []
    buffer = set()
    for doc in data:
        doc = base.Document.from_dict(doc, field_map=field_map) if isinstance(doc, dict) else doc
        if doc.id in buffer:
            continue
        buffer.add(doc.id)
        docs.append(doc)
    return docs


def flatten_list(nested_list):
    """Flatten an arbitrarily nested list, without recursion (to avoid
    stack overflows). Returns a new list, the original list is unchanged.
    >> list(flatten_list([1, 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]]))
    [1, 2, 3, 4, 5]
    >> list(flatten_list([[1, 2], 3]))
    [1, 2, 3]
    """
    nested_list = copy.deepcopy(nested_list)

    while nested_list:
        sublist = nested_list.pop(0)

        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist


def chunk(
    document: Union[dict, base.Document],
    chunk_length: int = 184,
    chunk_overlap: int = 64,
    on_dot: bool = True,
) -> List[dict]:
    """
    :param document:
    :return: List[Document]
    """

    def wrap_return(txt: List[str]) -> List[dict]:
        documents = []
        for i, txt in enumerate(txt_chunks):
            doc = copy.deepcopy(document)
            doc["text"] = txt
            if "meta" not in doc.keys() or doc["meta"] is None:
                doc["meta"] = {}
            doc["meta"]["chunk_id"] = i
            documents.append(doc)
        return documents

    if isinstance(document, base.Document):
        document = document.to_dict()
    text = document['text']
    sents = sentinize(text)
    if not on_dot:
        result = []
        segments = list([w for s in sents for w in s.text.split()])
        for seg in windowed(segments, n=chunk_length, step=chunk_length - chunk_overlap):
            result.append(' '.join(list(seg)))
        return wrap_return(result)
    word_cnt = 0
    chunks = []
    cur_chunk = []
    for sen in sents:
        cur_word_cnt = len(sen.text.split())
        if cur_word_cnt > chunk_length:
            logger.warning(
                f'Sentence \"{sen}\" contains {str(cur_word_cnt)} words. which is more than {str(chunk_length)}.'
            )
        if word_cnt + cur_word_cnt > chunk_length:
            if len(cur_chunk) > 0:
                chunks.append(cur_chunk)
            overlap = []
            cnt = 0
            for candidate in reversed(cur_chunk):
                seq_len = len(candidate.split())
                if cnt + seq_len < chunk_overlap:
                    overlap.append(candidate)
                    cnt += seq_len
                else:
                    break
            cur_chunk = list(reversed(overlap))
            word_cnt = cnt
        cur_chunk.append(str(sen))
        word_cnt += cur_word_cnt
    if cur_chunk:
        chunks.append(cur_chunk)
    txt_chunks = [' '.join(_chunk) for _chunk in chunks]

    return wrap_return(txt_chunks)
