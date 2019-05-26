from typing import List, Dict

from Model.violation import Violation


class CSPDB:
    __instance = None

    violation_list: List[Violation] = []


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    
    def __str__(self) -> str:
        retstr: str = ""
        retstr += "Violation: {violation_list}\n".format(violation_list=self.violation_list)
        return retstr

    
    def add_violation_list(self, violation: Violation) -> None:
        self.violation_list.append(violation)

    
    def get_violation_list(self) -> List[Violation]:
        return self.violation_list