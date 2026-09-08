from mysql import connector

class EmployeeManager:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Ashwin@123",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            
            return None
    def post(self):
        print("post method")
        pass