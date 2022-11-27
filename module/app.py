import os
from google.cloud import dialogflow_v2beta1 as dialogflow
from flask import Flask, request, jsonify, render_template
import json

def detect_intent_with_parameters(project_id, session_id, language_code, user_input):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text = user_input
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response

def input_text_stark(input_text):
    GOOGLE_AUTHENTICATION_FILE_NAME = "key.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

    GOOGLE_PROJECT_ID = "newagent-aesk"
    session_id = "1234567891"
    context_short_name = "does_not_matter"

    context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + context_short_name.lower()


    context_1 = dialogflow.Context(
        name=context_name,
        lifespan_count=2,
    )
    query_params_1 = {"contexts": [context_1]}

    language_code = 'en'

    response = detect_intent_with_parameters(
        project_id=GOOGLE_PROJECT_ID,
        session_id=session_id,
        language_code=language_code,
        user_input=input_text
    )
    
    result_json = response.__class__.to_json(response)
    response_dic = json.loads(result_json)['queryResult']
    # print(response_dic)
    com_stark = ""
    try:
     if response_dic['action'] == 'os.makedirectory':
        com_stark = "mkdir"
        com_stark += " "
        com_stark += response_dic['parameters']['folder-name']
    
     elif response_dic['action'] == 'os.removedirectory':
        com_stark = "rmdir"
        com_stark += " "
        try:
            com_stark += response_dic['parameters']['folder-name']
        except:
            com_stark += response_dic['parameters']['folder-remove']
     elif response_dic['action'] == 'os.cd':
        com_stark = "cd"
        com_stark += " "
        com_stark += response_dic['parameters']['cd']
     elif response_dic['action'] == 'os.ls':
        com_stark = "ls"
     elif response_dic['action'] == 'os.presentdirectory':
        com_stark = "pwd"
     elif response_dic['action'] == 'os.killstark':
        com_stark = "exit"
     elif response_dic['action'] == 'os.cat':
        com_stark = "cat"
        com_stark += " "
        com_stark += response_dic['parameters']['file-name']
     elif response_dic['action'] == 'os.clearscreen':
        com_stark = "clear"
     elif "smalltalk" in response_dic['action']:
        com_stark = response_dic['fulfillmentText']
    except:
        com_stark = "I didn't get that. Please try again."
    return com_stark, response_dic['action']
