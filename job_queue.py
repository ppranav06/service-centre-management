import sqlite3
import heapq

# Define the priorities and expertise
priorities = {
    "mileage problem": 1,
    "vibration problem": 1,
    "chain/belt problem": 1,
    "engine noise trouble": 1,
    "starting trouble": 1,
    "handle adjustment": 2,
    "mirror adjustment": 2,
}

class JobQueue:
    def __init__(self):
        self.queue = []
        self.job_map = {}

    def add_job(self, job_id, job_type, time_estimate):
        priority = priorities.get(job_type, float('inf'))
        job = (priority, job_id, job_type, time_estimate)
        heapq.heappush(self.queue, job)
        self.job_map[job_id] = job
   
    def get_next_job(self):
        while self.queue:
            priority, job_id, job_type, time_estimate = heapq.heappop(self.queue)
            if job_id in self.job_map:
                del self.job_map[job_id]
                return (priority, job_id, job_type, time_estimate)
        return None

    def remove_job(self, job_id):
        if job_id in self.job_map:
            job = self.job_map.pop(job_id)
            self.queue.remove(job)
            heapq.heapify(self.queue)

class EmployeeJobScheduler:
    def __init__(self):
        self.employees = {}
        # self.conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
        self.conn = sqlite3.connect('service-centre.db')  # Use in-memory database for testing
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assignments (
                employee_id TEXT,
                job_id TEXT,
                job_type TEXT,
                time_estimate INTEGER,
                PRIMARY KEY (employee_id, job_id)
            )
        ''')
        self.conn.commit()

    def add_employee(self, employee_id):
        if employee_id not in self.employees:
            self.employees[employee_id] = JobQueue()

    def add_job(self, employee_id, job_id, job_type, time_estimate):
        if employee_id not in self.employees:
            self.add_employee(employee_id)
        self.employees[employee_id].add_job(job_id, job_type, time_estimate)

    def get_next_job(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id].get_next_job()
        return None

    def remove_job(self, employee_id, job_id):
        if employee_id in self.employees:
            self.employees[employee_id].remove_job(job_id)

    def update_database(self, employee_id):
        if employee_id in self.employees:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM assignments WHERE employee_id = ?', (employee_id,))
            while self.employees[employee_id].queue:
                job = self.employees[employee_id].get_next_job()
                if job:
                    priority, job_id, job_type, time_estimate = job
                    cursor.execute('INSERT INTO assignments (employee_id, job_id, job_type, time_estimate) VALUES (?, ?, ?, ?)',
                                (employee_id, job_id, job_type, time_estimate))
            self.conn.commit()

    def employee_unavailable(self, employee_id):
        if employee_id in self.employees:
            next_job = self.get_next_job(employee_id)
            if next_job:
                priority, job_id, job_type, time_estimate = next_job
                self.remove_job(employee_id, job_id)

    def close(self):
        self.conn.close()

# Test code
def test_job_scheduler():
    scheduler = EmployeeJobScheduler()
    scheduler.add_employee("E1")
    scheduler.add_employee("E2")

    # Adding assignments to employee E1
    scheduler.add_job("E1", "J1", "mileage problem", 3)
    scheduler.add_job("E1", "J2", "handle adjustment", 2)
    scheduler.add_job("E1", "J3", "engine noise trouble", 4)

    # Adding assignments to employee E2
    scheduler.add_job("E2", "J4", "vibration problem", 1)
    scheduler.add_job("E2", "J5", "mirror adjustment", 5)
    scheduler.add_job("E2", "J6", "starting trouble", 3)

    print("Next job for E1:", scheduler.get_next_job("E1")) 
    print("Next job for E2:", scheduler.get_next_job("E2")) 

    # Update database with current job queue state
    scheduler.update_database("E1")
    scheduler.update_database("E2")

    # Adding assignments back to queue to simulate persistence after DB update
    scheduler.add_job("E1", "J2", "handle adjustment", 2)
    scheduler.add_job("E1", "J3", "engine noise trouble", 4)
    scheduler.add_job("E2", "J5", "mirror adjustment", 5)
    scheduler.add_job("E2", "J6", "starting trouble", 3)

    # Removing a job and re-checking
    scheduler.remove_job("E1", "J2")
    scheduler.remove_job("E2", "J6")
    print("Next job for E1 after removing J2:", scheduler.get_next_job("E1")) 
    print("Next job for E2 after removing J6:", scheduler.get_next_job("E2")) 

    # Clean up
    scheduler.close()

# Run the test
test_job_scheduler()
