class QuestionAnswer:
    def __init__(self, id, question, answer=None, q_type=None):
        self.id = id
        self.question = question
        self.answer = answer
        self.q_type = q_type

    @classmethod
    def from_firebase(cls, firebase_doc):
        return cls(
            id=firebase_doc.id,
            question=firebase_doc.get('question'),
            answer=firebase_doc.get('answer'),
            q_type=firebase_doc.get('type')
        )

    @classmethod
    def from_postgres(cls, row):
        return cls(
            id=row[0],
            question=row[1],
            answer=row[2],
            q_type=row[3]
        )
