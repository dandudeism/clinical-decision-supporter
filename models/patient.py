class Patient:
    def __init__(self, age=int, heart_rate=int, systolic_bp=int, temperature=float, resp_rate=int, sats=int, confusion=bool):
        self.age = age
        self.heart_rate = heart_rate
        self.systolic_bp = systolic_bp
        self.temperature = temperature
        self.resp_rate = resp_rate
        self.sats = sats
        self.confusion = confusion
