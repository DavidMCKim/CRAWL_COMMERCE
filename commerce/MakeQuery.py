import pandas as pd
from google.cloud import spanner

def query_data(instance_id, database_id):
    """Queries sample data from the database using SQL."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            """
            """
        )

        df = pd.DataFrame(columns=['Channelname','Device','Placement','Round','Count'])
        for row in results:
            df.loc[len(df)] = row
    # print(df)
    return df