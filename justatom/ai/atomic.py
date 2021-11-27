import catboost
from justatom.ai import interface


class AtomicAI(interface.AI):
    def __init__(self):
        self.booster = None
        self.bert_encoder = None

    def predict(self, txt: str, **kwargs):
        return [{"confidence": str(0.2077), "description": str("Без шансов, бро")}]
