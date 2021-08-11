import justpy as jp
import definition
import json

class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        meaning = definition.Definition(word).get()

        response = {
            "word":word,
            "definition":meaning
        }

        wp.html = json.dumps(response)
        return wp

