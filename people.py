# the type of employees that you will have



class Employee:    
    def __init__(self, name, position, skills, salary):
        self.name = name
        self.position = position
        self.skills = skills
        self.salary = salary
        self.happiness = 100  # default happiness level


class Mechanic (Employee):    
    def __init__(self, specialty, **kwargs):
        super().__init__(**kwargs)
        self.specialty = specialty

class Pilot (Employee):
    def __init__(self, licenseLevel, **kwargs):
        super().__init__(**kwargs)
        self.licenseLevel = licenseLevel

class Intel (Employee):
    def __init__(self, fieldOfStudy, **kwargs):
        super().__init__(**kwargs)
        self.fieldOfStudy = fieldOfStudy

class Chef (Employee):
    def __init__(self, cuisineSpecialty, **kwargs):
        super().__init__(**kwargs)
        self.cuisineSpecialty = cuisineSpecialty



class Skills:    
    def __init__(self, communication, strategy, technique, awareness, knowledge):
        self.communication = communication
        self.strategy = strategy
        self.technique = technique
        self.awareness = awareness
        self.knowledge = knowledge


class PilotSkills (Skills):    
    def __init__(self, reflexes, positioning, melee, aim, resilience, **kwargs):
        super().__init__(**kwargs)
        self.reflexes = reflexes
        self.positioning = positioning
        self.melee = melee
        self.aim = aim
        self.resilience = resilience

class MechanicSkills (Skills):
    def __init__(self, repair, diagnostics, fabrication, maintenance, **kwargs):
        super().__init__(**kwargs)
        self.repair = repair
        self.diagnostics = diagnostics
        self.fabrication = fabrication
        self.maintenance = maintenance

class IntelSkills (Skills):
    def __init__(self, analysis, research, espionage, cryptography, surveillance, **kwargs):
        super().__init__(**kwargs)
        self.analysis = analysis
        self.research = research
        self.espionage = espionage
        self.cryptography = cryptography
        self.surveillance = surveillance

class ChefSkills (Skills):
    def __init__(self, cooking, baking, plating, nutrition, menuPlanning, **kwargs):
        super().__init__(**kwargs)
        self.cooking = cooking
        self.baking = baking
        self.plating = plating
        self.nutrition = nutrition
        self.menuPlanning = menuPlanning