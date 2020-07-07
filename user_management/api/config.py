import os


class Config(object):
    """Parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class LocalConfig(Config):
    """Configuration for development on localhost"""
    DEBUG = True
    VERSION_MAJOR = 1
    VERSION_MINOR = 0
    VERSION_PATCH = 0


class TestingConfig(Config):
    """Configuration for testing locally with a separate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True
    VERSION_MAJOR = 1
    VERSION_MINOR = 0
    VERSION_PATCH = 0


class ProductionConfig(Config):
    """Production configuration values"""
    DEBUG = False
    TESTING = False
    VERSION_MAJOR = 1
    VERSION_MINOR = 0
    VERSION_PATCH = 0


app_config = {
    'local': LocalConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
