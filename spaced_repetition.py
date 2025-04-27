# File: src/spaced_repetition.py

import datetime

class SpacedRepetition:
    def __init__(self):
        # stores {concept: last_review_datetime}
        self.review_schedule = {}

    def add_concept(self, concept: str):
        """Add or update a concept's review timestamp to now."""
        self.review_schedule[concept] = datetime.datetime.now()

    def get_due_reviews(self, days_interval: int = 1):
        """
        Return all concepts whose last review was at least `days_interval` ago.
        """
        now = datetime.datetime.now()
        due = []
        for concept, last in self.review_schedule.items():
            if (now - last).days >= days_interval:
                due.append(concept)
        return due
