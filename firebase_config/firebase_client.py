import firebase_admin
from firebase_admin import credentials, firestore

from project.backend.models.question_answer import QuestionAnswer


class FirebaseClient:
    def __init__(self, cred_url):
        self.credentials_url = cred_url
        self.initialize_firebase()

    def fetch_credentials_from_url(self):
        import requests
        try:
            print(f"Downloading Firebase credentials from URL: {self.credentials_url}")
            response = requests.get(self.credentials_url)
            if response.status_code == 200:
                return response.json()  # Parse the JSON content directly
            else:
                raise Exception(f"Failed to download credentials. HTTP Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading credentials from URL: {e}")
            raise

    def initialize_firebase(self):
        try:
            # Avoid reinitializing if the default app already exists
            if not firebase_admin._apps:
                credentials_json = self.fetch_credentials_from_url()
                cred = credentials.Certificate(credentials_json)
                firebase_admin.initialize_app(cred)
                print("Firebase initialized successfully.")
            else:
                print("Firebase already initialized.")
            self.db = firestore.client()
        except Exception as e:
            print(f"Error initializing Firebase: {e}")
            raise

    def fetch_all_questions(self, collection_name="questions"):
        try:
            questions_ref = self.db.collection(collection_name)
            docs = questions_ref.stream()
            questions = []
            for doc in docs:
                print(doc.to_dict())
                questions.append(QuestionAnswer.from_firebase(doc))
            return questions
        except Exception as e:
            print(f"Error fetching questions: {e}")
            return []

