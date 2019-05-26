from typing import Optional


class Violation:
    def __init__(self, category: int, filename: str, line: Optional[int]):
        self.category: int = category
        self.filename: str = filename
        self.line: Optional[int] = line


    def __str__(self) -> str:
        return "{category} @ {filename}:{line}".format(category=self.category,
                                                       filename=self.filename,
                                                       line=self.line)


    def get_category(self) -> int:
        return self.category

    
    def get_filename(self) -> str:
        return self.filename


    def get_line(self) -> Optional[int]:
        return self.line
