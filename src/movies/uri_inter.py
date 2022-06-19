from abc import ABC, abstractmethod


class UriInter(ABC):
    @abstractmethod
    def get_postgres_uri():
        pass
