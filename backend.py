import heapq
from datetime import datetime
import sqlite3

db = sqlite3.connect('service-centre.db')
c = db.cursor()

class JobCard:
    def __init__(self, job_id, registration_number, owner_details, engine_number, service_type, expected_delivery_date, priority):
        self.job_id = job_id
        self.registration_number = registration_number
        self.owner_details = owner_details
        self.engine_number = engine_number
        self.service_type = service_type
        self.expected_delivery_date = expected_delivery_date
        self.priority = priority  # Lower number means higher priority
        self.status = 'Pending'

    def __lt__(self, other):
        """For comparison of priorities"""
        return self.priority < other.priority

    def get_data(self):
        return (self.job_id, self.registration_number, self.owner_details, self.engine_number, self.service_type, self.expected_delivery_date, self.priority, self.status)
    

class CustomerCard:
    def __init__(self, vehicle_no, name, address, mail_id, phone_no, phone_no_2 = None):
        # self.customer_id = customer_id
        self.vehicle_no = vehicle_no
        self.name = name
        self.address = address
        self.mail_id = mail_id
        self.phone_no = phone_no
        self.phone_no_2 = phone_no_2
    
    def __repr__(self) -> str:
        return ",".join([self.vehicle_no, self.name, self.address, self.mail_id, self.phone_no, self.phone_no_2])
    
    @classmethod
    def get_customer(self, vehicle_no:str):
        """Fetching data for entering vehicle in job card"""
        # c.execute(f"SELECT * FROM customers WHERE vehicle_no={vehicle_no};")
        c.execute(f"SELECT vehicle_no, name FROM customers;")
        return c.fetchall()

class EmployeeCard:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.job_list = []

    def assign_job(self, job_card):
        self.job_list.append(job_card)

class JobPriorityQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, job_card):
        heapq.heappush(self.queue, job_card)

    def get_next_job(self):
        return heapq.heappop(self.queue) if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

def calculate_priority(job_card):
    """Lower number means higher priority, just like nice value"""
    service_priority = {
        'brake repair': 1,
        'engine repair': 2,
        'oil change': 3,
        'general maintenance': 4
    }

    delivery_date_priority = (job_card.expected_delivery_date - datetime.now()).days
    service_type_priority = service_priority.get(job_card.service_type, 5)
    
    return delivery_date_priority + service_type_priority

if __name__=='__main__':
    # Create some example job cards
    job1 = JobCard(
        job_id=1,
        registration_number='ABC123',
        owner_details=CustomerCard('John Doe', '1/50, Rengarajan St, Kovilambakkam, Chennai - 600117', '6564889953'),
        engine_number='ENG123',
        service_type='brake repair',
        expected_delivery_date=datetime(2024, 5, 25),
        priority=0  # Initial placeholder
    )
    job1.priority = calculate_priority(job1)

    job2 = JobCard(
        job_id=2,
        registration_number='XYZ456',
        owner_details='Jane Smith',
        engine_number='ENG456',
        service_type='oil change',
        expected_delivery_date=datetime(2024, 5, 26),
        priority=0  # Initial placeholder
    )
    job2.priority = calculate_priority(job2)

    # Create the priority queue and add jobs
    priority_queue = JobPriorityQueue()
    priority_queue.add_job(job1)
    priority_queue.add_job(job2)

    # Assign jobs to a mechanic
    mechanic = EmployeeCard(employee_id=1, name='Mike')

    while not priority_queue.is_empty():
        next_job = priority_queue.get_next_job()
        mechanic.assign_job(next_job)
        print(f"Assigned job {next_job.job_id} to {mechanic.name}")

    # Output the mechanic's assigned jobs
    for job in mechanic.job_list:
        print(f"Mechanic {mechanic.name} has job {job.job_id} with priority {job.priority}")