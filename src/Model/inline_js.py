class InlineJS:
    def __init__(self, source_code: str):
        self.source_code: str = source_code

    
    def __str__(self) -> str:
        return "Inline JavaScript: " + (self.source_code if len(self.source_code) < 20 else self.source_code[:17] + "...")


    def get_source_code(self) -> str:
        return self.source_code