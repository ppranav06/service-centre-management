# service-centre-management

A Job Management System equipped for a two-wheeler service centre, written in Python and Tkinter

Problem Statement
---

A two-wheeler service shop wants to develop a system to regulate the maintenance of their day-to-day services. Every incoming vehicle must be assigned a job card. The card should have various details such as registration number, owner details, engine number, type of service needed, and expected delivery date. Further information to be filled in the job card varies as per the service type (Ex: maintenance, oil service, brake condition etc.). On completing the vehicle service, the job card has to be updated, and the system has to alert the owner automatically. The job's priority is fixed based on specific criteria like delivery date, and a service mechanic gets the list of jobs for the day. 

Installation Instructions
---

In order to run the software, follow the below instuctions:
1. Obtain all dependencies 

    Windows: 
    ```
    winget install Git.Git Python
    ```
    Linux:
    ```
    sudo apt install python python3-pip git
    ```

    Install tkinter module:
    ```
    pip install tkinter
    ```

2. Clone the repository
    ```
    git clone https://github.com/ppranav06/service-centre-management.git
    ```

3. Run the file `Home-page.py`
    ```
    python3 ./Home-page.py
    ```