import pandas as pd
from time import time
from sqlalchemy import create_engine
from dataclasses import dataclass
from argparse import ArgumentParser


class NoData(Exception):
    pass


@dataclass
class PSQLConnection:
    user: str
    password: str
    host: str
    port: str
    db_name: str

    def create_connection(self):
        db_uri = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        return create_engine(db_uri)


def load_data(data_url: str):
    try:
        df_iter = pd.read_parquet(data_url)
    except:
        raise NoData(f"Not able to load data from {data_url}")
    return df_iter


def chunks(df: pd.DataFrame, chuck_size: int) -> pd.DataFrame:
    """Splits a dataframe in chunks.

    Args:
        df (pd.DataFrame): dataframe to split
        chuck_size (int): size of the chunk.

    Yields:
        pd.DataFrame: chunked dataframe
    """
    for i in range(0, len(df), chuck_size):
        yield df.iloc[i : i + chuck_size]


def write_to_db(engine, frame: pd.DataFrame, table_name: str, chunk_size: int) -> None:
    for idx, chunk in enumerate(chunks(frame, chunk_size)):
        if idx == 0:
            if_exists_param = "replace"

        else:
            if_exists_param = "append"

        chunk.to_sql(con=engine, name=table_name, if_exists=if_exists_param)


def generate_url(year: str, month: str) -> str:
    return f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"


def cli() -> ArgumentParser:

    parser = ArgumentParser(description="Ingest PARQUET data to Postgres")
    parser.add_argument("--user", required=True, help="user name for postgres")
    parser.add_argument("--password", required=True, help="password for postgres")
    parser.add_argument("--host", required=True, help="host for postgres")
    parser.add_argument("--port", required=True, help="port for postgres")
    parser.add_argument("--db", required=True, help="database name for postgres")
    parser.add_argument(
        "--table_name",
        required=True,
        help="name of the table where we will write the results to",
    )
    parser.add_argument("--year", required=True, help="year of the dataset")
    parser.add_argument("--month", required=True, help="month of the dataset")
    return parser.parse_args()


def add_data_to_psql(engine, table_name: str, data_url: str):
    df = load_data(data_url)
    write_to_db(engine, frame=df, table_name=table_name, chunk_size=100_000)


if __name__ == "__main__":
    args = cli()

    engine = PSQLConnection(
        user=args.user,
        password=args.password,
        host=args.host,
        port=args.port,
        db_name=args.db,
    ).create_connection()

    data_url = generate_url(year=args.year, month=args.month)

    add_data_to_psql(engine=engine, table_name=args.table_name, data_url=data_url)
