from dataclasses import dataclass


@dataclass
class DataToFill:
    full_name: str = None
    mail: str = None
    current_address: str = None
    permanent_address: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: str = None


@dataclass
class DataToColor:
    color: str = None


@dataclass
class DataToDate:
    year: str = None
    month: str = None
    day: str = None
    tim: list = None

