import os
from uri_inter import UriInter


class PostgresURI(UriInter):
    def get_postgres_uri():
        host = os.environ.get("DB_HOST", "postgres")
        port = 5432
        password = os.environ.get("DB_PASS", "abc123")
        user, db_name = "movies", "movies"
        return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
