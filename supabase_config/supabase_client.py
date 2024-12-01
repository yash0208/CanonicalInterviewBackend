# supabase_client.py

from supabase import create_client, Client
import os

class SupabaseClient:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.client = self.initialize_supabase()

    def initialize_supabase(self) -> Client:
        try:
            # Initialize the Supabase client with the URL and API Key
            client = create_client(self.url, self.api_key)
            return client
        except Exception as e:
            print(f"Error initializing Supabase: {e}  {self.url}")
            raise

    def fetch_all_questions(self, table_name="questions"):
        try:
            # Fetch questions from the "questions" table in Supabase
            questions_data = self.client.table(table_name).select("*").execute()
            return questions_data.data
        except Exception as e:
            print(f"Error fetching questions from Supabase: {e}")
            return []

