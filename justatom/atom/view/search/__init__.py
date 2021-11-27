import logging

from flask import jsonify, request
from icecream import ic
from justatom.ai import ai

from .view import search

logger = logging.getLogger(__name__)


@search.route('/search', methods=['POST'])
def atom_search():
    data = request.get_data(parse_form_data=True).decode('utf-8-sig')
    ic(data)
    response = ai.predict(data)
    return jsonify(response)
    # return jsonify([{"confidence": str(0.2077), "description": str("Без шансов, бро")}])
