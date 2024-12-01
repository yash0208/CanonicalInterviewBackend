import os
from http.client import responses

from boto3 import s3
from firebase_admin.exceptions import FirebaseError
from flask import Blueprint, jsonify

from firebase_config.firebase_client import FirebaseClient
from supabase_config.supabase_client import SupabaseClient

supabase_url = os.getenv("SUPABASE_URL")
supabase_api_key = os.getenv("SUPABASE_API_KEY")
cred_url = os.getenv('CRED_URL')


# Create a Blueprint for the API
api_gateway = Blueprint('api_gateway', __name__)

@api_gateway.route('/', methods=['GET'])
def welcome():
    try:
        response={
            "message": "Welcome"
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_gateway.route('/questions/technical', methods=['GET'])
def get_technical_questions():
    try:
        # Fetch all technical questions from Supabase
        print("calling url "+supabase_url)
        supabase_client = SupabaseClient(supabase_url, supabase_api_key)
        questions = supabase_client.fetch_all_questions()
        response = [{"id": q["id"], "question": q["question"], "answer": q["answer"], "type": q["type"]} for q in questions]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_gateway.route('/questions/nontechnical', methods=['GET'])
def get_nontechnical_questions():
    try:
        # Fetch all non-technical questions from Firebase
        firebase_client = FirebaseClient(cred_url)

        questions = firebase_client.fetch_all_questions()
        response = [{"id": q.id, "question": q.question, "answer": q.answer, "type": q.q_type} for q in questions]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
