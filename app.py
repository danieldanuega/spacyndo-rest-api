from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
import spacy
from spacy import displacy
from pathlib import Path

app = Flask(__name__)
api = Api(app)

# Load the model
nlp = spacy.load('id_ud-tag-dep-ner-1.0.0')


class Tasks(Resource):

    def post(self, task):
        req = reqparse.RequestParser()
        req.add_argument("text")
        args = req.parse_args()

        doc = nlp(args["text"])

        if(task == "dep"):
            svg = displacy.render(doc, style="dep")
            output_path = Path('graph/dep.svg')
            output_path.open("w", encoding="utf-8").write(svg)
            return send_from_directory('graph/','dep.svg')

        elif(task == "ner"):
            result = []
            for ent in doc.ents:
                result.append((ent.text,ent.label_))
            return result

        else:
            return "Task Not Found", 404


api.add_resource(Tasks, "/tasks/<string:task>")


if __name__ == '__main__':
    app.run()