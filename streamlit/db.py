from sqlite3 import connect

DB_NAME = "MoviesApiInfo.db"


def init_db():
    query = """
    CREATE TABLE IF NOT EXISTS MoviesData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER,
        imdb_rate REAL,
        genres TEXT,
        poster TEXT
    )
    """

    with connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query)


def insert_record(title, year, imdb_rate, genres, poster):
    query = """
    INSERT INTO MoviesData (
        title,
        year,
        imdb_rate,
        genres,
        poster
    )
    VALUES (?, ?, ?, ?, ?)
    """

    with connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            query,
            (
                title,
                year,
                imdb_rate,
                genres,
                poster
            )
        )


def insert_list_of_movies(movies_list):
    records = []

    for item in movies_list:
        records.append(
            (
                item.get("title"),
                item.get("year"),
                item.get("imdb_rate"),
                ",".join(item.get("genres", [])),
                item.get("poster")
            )
        )

    query = """
    INSERT INTO MoviesData (
        title,
        year,
        imdb_rate,
        genres,
        poster
    )
    VALUES (?, ?, ?, ?, ?)
    """

    with connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.executemany(query, records)

    return f"{len(records)} records inserted successfully."