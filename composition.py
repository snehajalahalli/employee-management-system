class Engine:
    def start(self):
        print("StartEngine")

class Car:

    def __init__(self):
        self.engine=Engine()

    def start(self):
        self.engine.start()

car=Car()
car.start()

class SkillExtractor:
    def skills(self):
        print("skills")

class JobMatcher:
    def __init__(self):
        self.skillextractor=SkillExtractor()

    def skills(self):
        self.skillextractor.skills()

class ResumeParser:
    def upload(self):
        print("upload resume")

jm=JobMatcher()
jm.skills()