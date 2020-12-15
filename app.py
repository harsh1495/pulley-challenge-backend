import json
from flask import Flask, request, abort
from flask_cors import CORS

from response import Response
from document_preprocessor import DocumentPreprocessor
from document_similarity import DocumentSimilarity

app = Flask(__name__)

# globals
SEARCH_RESULTS_SIZE_PER_PAGE = 10
SEARCH_RESULTS_START_POSITION = 1

# response object
res = Response()

# cross-origin resource sharing
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PATCH,POST,DELETE,OPTIONS')
    return response


@app.route("/search", methods=["GET"])
def get_search_results():
    '''
    Fetch a list of pages that match closely with the search query
    '''
    query = request.args.get("q")
    start = int(request.args.get("start", SEARCH_RESULTS_START_POSITION))
    size = int(request.args.get("size", SEARCH_RESULTS_SIZE_PER_PAGE))

    if not query:
        data = res.get_error_response_no_results()
        return json.dumps(data), 200

    try:
        query_processor_obj = DocumentPreprocessor(query)
        processed_query = query_processor_obj.process_document_text()

        if not processed_query:
            data = res.get_error_response_no_results()
            return json.dumps(data), 200

        doc_similarity_obj = DocumentSimilarity(processed_query)
        top_search_pages = doc_similarity_obj.generate_search_results()

        if not top_search_pages:
            data = res.get_error_response_no_results()
            return json.dumps(data), 200

        print(len(top_search_pages))
        data = res.format_results(top_search_pages, start, size)
        return json.dumps({"results": data, "total_count": len(top_search_pages), "current_count": len(data)}), 200

    except:
        error = res.get_error_response("An error occurred")
        return json.dumps(error), 500

# Error Handling


@app.errorhandler(404)
def not_found_404(error):
    error = res.get_error_response("Resource not found")
    return json.dumps(error), 404


@app.errorhandler(400)
def bad_request_400(error):
    error = res.get_error_response("Bad request")
    return json.dumps(error), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
