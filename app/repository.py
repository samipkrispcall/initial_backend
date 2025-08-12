from abc import ABC, abstractmethod
from typing import List
from app.models import PERSONS


class PersonRepository(ABC):
    @abstractmethod
    async def list_names(self) -> List[str]:
        pass


class InMemoryPersonRepository(PersonRepository):
    async def list_names(self) -> List[str]:
        return [person.name for person in PERSONS]
