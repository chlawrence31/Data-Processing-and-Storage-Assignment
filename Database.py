class Database:
    def __init__(self):
        self.data = {}
        self.transaction_in_progress = False
        self.transaction_data = {}

    def begin_transaction(self):
        if self.transaction_in_progress:
            return "Error transaction already in progress"
        self.transaction_in_progress = True
        self.transaction_data = {}
        return "Transaction started"

    def put(self, key, value):
        if not self.transaction_in_progress:
            return "Error transaction not in progress"
        self.transaction_data[key] = value
        return "Succesfull put"

    def get(self, key):
        if key in self.data:
            return self.data[key]
        return "Null, no data found"

    def commit(self):
        if not self.transaction_in_progress:
            return "Error Transaction not in progress"
        self.data.update(self.transaction_data)
        self.transaction_data.clear()
        self.transaction_in_progress = False
        return "Successfully committed"

    def rollback(self):
        if not self.transaction_in_progress:
            return "Error transaction not in progress"
        self.transaction_data.clear()
        return "Successfully rolledbacked"


# Example usage:
db = Database()
#Test 1
print(db.get("A"))
#Test 2
print(db.put("A", 5))
#Test 3
print(db.begin_transaction())
#Test 4
print(db.put("A", 5))
#Test 5
print(db.get("A"))
#Test 6
print(db.put("A", 6))
#Test 7
print(db.commit())
#Test 8
print(db.rollback())
#Test 9
print(db.get("A"))
#Test 10
print(db.get("B"))
#Test 11
print(db.begin_transaction())
#Test 12
print(db.put("B", 10))
#Test 13
print(db.rollback())
#Test 14
print(db.get("B"))