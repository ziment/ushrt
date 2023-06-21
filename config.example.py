class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

    HASHIDS_SALT = "this should be a secret random string"
    HASHIDS_MIN_LENGTH = 4
