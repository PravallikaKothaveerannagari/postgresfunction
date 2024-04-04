import logging
import os

import azure.functions as func
import psycopg2

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="ping_db", auth_level=func.AuthLevel.FUNCTION)
def ping_db(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sample_sql = "SELECT * FROM inventory;"

    # cnx_str = "user=Pravallika, password=Pr@vu$25o8, host=postgreserver0404.postgres.database.azure.com, dbname=postgres"
    with psycopg2.connect(
    host='postgreserver0404.postgres.database.azure.com',
    dbname='postgres',
    user='Pravallika',
    password='Pr@vu$25o8',
    sslmode='require') as cnx:
        cursor = cnx.cursor()
        cursor.execute(sample_sql)
        result = cursor.fetchone()
        cursor.close()

    return func.HttpResponse(f"{result}")


@app.route(route="sanity_check", auth_level=func.AuthLevel.FUNCTION)
def sanity_check(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse("sanity_check")