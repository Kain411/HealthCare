from flask import current_app
from model import Chat
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
knowledge_path = os.path.join(current_dir, 'data', 'knowledge.json')
with open(knowledge_path, 'r', encoding='utf-8') as f:
    knowledge_data = json.load(f)

def get_symptom_controller():
    symptoms = []
    for data in knowledge_data:
        for symptom in data.get('symptoms'):
            if symptom not in symptoms:
                symptoms.append(symptom)
    
    return sorted(symptoms)


def get_diseases_controller(symptoms):
    res = []
    for disease in knowledge_data:
        ok = True
        for symptom in symptoms:
            if symptom not in disease.get('symptoms'):
                ok = False
                break
        if ok: res.append(disease)

    return res