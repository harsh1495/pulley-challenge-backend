import os
import codecs
from global_variables import PLAYS_DIRECTORY


class Response:
    def __init__(self):
        self.error_msg = None

    @staticmethod
    def pagination(data, start, size):
        if start > len(data):
            return []

        start_idx = start
        end_idx = start_idx + size

        return data[start_idx:end_idx]

    def get_error_response(self, msg):
        '''
        Create an error response to send to the client
        '''
        self.error_msg = msg
        response = {
            "success": False,
            "error": self.error_msg
        }

        return response

    def get_error_response_no_results(self, msg=None):
        '''
        Create a response to send to the client when the search query is empty or does not produce any results
        '''
        if not msg:
            self.error_msg = "Sorry, we could not find anything for your search query. Please try again with a more specific query."
        else:
            self.error_msg = msg

        response = {
            "success": True,
            "error": self.error_msg
        }

        return response

    def format_results(self, results, start, size):
        data = []
        paginated_results = Response.pagination(results, start, size)
        for result in paginated_results:
            filepath = os.path.join(PLAYS_DIRECTORY, result[1], result[0])
            with codecs.open(filepath, 'r', encoding="utf-8", errors="ignore") as file:
                content = file.read()

            data.append({
                "book": result[1].replace("_", " "),
                "raw_content": content.lstrip("\n")
            })

        return data
