from dataclasses import dataclass


@dataclass
class DataToFill:
    full_name: str = None
    mail: str = None
    current_address: str = None
    permanent_address: str = None
