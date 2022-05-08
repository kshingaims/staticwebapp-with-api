import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = {
              "input": req_body.get('name'),
              "message": "Hello, " + req_body.get('name') + ". This HTTP triggered function executed successfully."
            }

    if name:
        return func.HttpResponse(
          json.dumps(name),
          mimetype="application/json" 
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )