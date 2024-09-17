from enum import Enum
import os


class Config:

    MAX_USERS = os.getenv('MAX_USERS', default=20)
    MIN_USERS = os.getenv('MIN_USERS', default=0)


class DevelopmentConfig(Config):

    pass


class ProductionConfig(Config):

    pass


class ConfigType(Enum):
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'

    @classmethod
    def reverse_lookup(cls, value):
        """Reverse lookup."""
        for _, member in cls.__members__.items():
            if member.value == value:
                return member
        raise LookupError


class ConfigFactory:
    _configs = {
        ConfigType.DEVELOPMENT: DevelopmentConfig,
        ConfigType.PRODUCTION: ProductionConfig
    }
    current = None

    def get(self, type_: ConfigType):
        cls = self._configs[type_]
        self.current = cls()
        return self.current
