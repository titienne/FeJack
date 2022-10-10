import jack

class FeJack:
    def __init__(self) -> None:
        self.jackConn = jack.Client('FeJack')
        