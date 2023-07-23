class Patient:
    def __init__(self,name,age,visit_date,reason):
        self.patient_name = name
        self.patient_age = age
        self.patient_visitdate = visit_date
        self.reason = reason
        
    def add_patient(self):
        print("Name: "+self.patient_name)
        print("Age: "+str(self.patient_age))
        print("Date Of Visit: "+self.patient_visitdate)
        print("Reason For Visit: "+self.reason)
        print("Patient Added")
        
patient1 = Patient("Jeff",78,"11/09/2001","Itchy Bum")
patient1.add_patient()

Patient2 = Patient("Gerald",25,"21/04/2010","Rash On Leg")
Patient2.add_patient()
