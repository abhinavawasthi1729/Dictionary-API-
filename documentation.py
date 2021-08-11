import justpy as jp

class Doc():

    @classmethod
    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp,  classes = "bg-gray-200 h-screen")
        jp.Div(a = div, text= "Dictionary API", 
                classes = "text-4xl m-2" )
        jp.Div(a=div, text = "Get definiton of word", classes = "text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text = "http://127.0.0.1:8000/api?w=abort")
        jp.Hr(a=div)
        jp.Div( a = div, text ="""
        {"word": "abort", 
        "definition": ["To miscarry; to bring forth young prematurely.", 
        "To become checked in normal development, so as either to remain rudimentary or shrink away wholly; to become sterile.", 
        "An untimely birth.", "An aborted offspring."]}
        
        """, classes= "text-lg p-2")
        return wp

