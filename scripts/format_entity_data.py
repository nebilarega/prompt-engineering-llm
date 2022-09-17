import json
import pprint

def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def format_data(original_filepath, new_file_path): 
    data_json = load_json(original_filepath)
    entity_labels = ['DIPLOMA', 'DIPLOMA_MAJOR', 'EXPERIENCE', 'SKILLS']
    final_string = []
    with open(new_file_path, 'w') as w:
        for d in data_json:
            document = d['document']
            dic = dict()
            dic["Document"] = document
            dic['DIPLOMA'] = []
            dic['DIPLOMA_MAJOR'] = []
            dic['EXPERIENCE'] = []
            dic['SKILLS'] = []
            for token in d['tokens']:
                if token['entityLabel'] in entity_labels:
                    dic[token['entityLabel']].append(token['text'])
            final_string.append(dic)
        for dc in final_string:
            w.write('Job post: ' + dc['Document'] + '\n')
            w.write("Extracted diploma from job post: " + ",".join(dc['DIPLOMA']) + '\n')
            w.write("Extracted major of diploma from job post: " + ",".join(dc['DIPLOMA_MAJOR']) + '\n')
            w.write("Extracted experience from job post: " + ",".join(dc['EXPERIENCE']) + '\n')
            w.write("Extracted skills from job post: " + ",".join(dc['SKILLS']) + '\n')
            w.write('---SEPARATOR---\n')
        
format_data("data/entity_document.json", "data/entity_docuemnt.txt")