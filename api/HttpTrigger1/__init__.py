import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    if text:
        upper_text = text.upper()
        return func.HttpResponse(f"The uppercase of the given text is: {upper_text}")
    else:
        return func.HttpResponse(
             "Please pass a text on the query string or in the request body",
             status_code=400
        )
