class SystemeExpert:
    def __init__(self):
        self.faits = []
        self.regles = []
        self._historique = []
    
    def afficheFaits(self):
        if not self.faits:
            print("No facts in the database.")
        else:
            print("Known facts:", self.faits)
    
    def ajouteFait(self, fait):
        if fait not in self.faits:
            self.faits.append(fait)
            print(f"Fact added: {fait}")
            return True
        print(f"Fact '{fait}' already exists.")
        return False
    
    def initDBs(self):
        self.faits = []
        self.regles = []
        self._historique = []
        print("Databases cleared successfully.")
    
    def afficheRegles(self):
        if not self.regles:
            print("No rules in the database.")
        else:
            print("Rules in database:")
            for i, regle in enumerate(self.regles, 1):
                print(f"  R{i}: IF {regle[0]} THEN {regle[1]}")
    
    def ajouteRegle(self, conditions, consequence):
        regle = [conditions, consequence]
        self.regles.append(regle)
        print(f"Rule added: IF {conditions} THEN {consequence}")
    
    def conditionsRegle(self, regle):
        return regle[0]
    
    def consequenceRegle(self, regle):
        return regle[1]
    
    def satisfaitUneCondition(self, regle, le_fait):
        return le_fait in self.conditionsRegle(regle)
    
    def satisfaitConditions(self, regle):
        for condition in self.conditionsRegle(regle):
            if condition not in self.faits:
                return False
        return True
    
    def chainageAvantSimple(self, faitsInitiaux, regles=None):
        self.faits = faitsInitiaux.copy()
        self._historique = []
        
        if regles is None:
            regles = self.regles
        
        cycle = 1
        nouveauFait = True
        
        print("\n" + "=" * 50)
        print("FORWARD CHAINING STARTED")
        print("=" * 50)
        print(f"Initial facts: {self.faits}\n")
        
        while nouveauFait:
            nouveauFait = False
            print(f"--- Cycle {cycle} ---")
            
            for i, regle in enumerate(regles, 1):
                if self.satisfaitConditions(regle):
                    consequence = self.consequenceRegle(regle)
                    
                    if consequence not in self.faits:
                        print(f"  Firing R{i}: {self.conditionsRegle(regle)} -> {consequence}")
                        self.faits.append(consequence)
                        nouveauFait = True
                        
                        self._historique.append({
                            'cycle': cycle,
                            'rule_num': i,
                            'conditions': self.conditionsRegle(regle).copy(),
                            'new_fact': consequence
                        })
            
            cycle += 1
            
            if cycle > 20:
                print("Stopped: maximum cycles reached (20)")
                break
        
        print(f"\nFinal facts: {self.faits}")
        return self.faits
    
    def trace(self):
        if not self._historique:
            print("No trace available. Run chainageAvantSimple first.")
            return
        
        print("\n" + "=" * 50)
        print("INFERENCE TRACE")
        print("=" * 50)
        
        for step in self._historique:
            print(f"Cycle {step['cycle']}: Fired Rule R{step['rule_num']}")
            print(f"         Conditions: {step['conditions']}")
            print(f"         New fact deduced: {step['new_fact']}")
            print("-" * 40)


if __name__ == "__main__":
    print("=" * 60)
    print("EXAMPLE: Weather Expert System")
    print("=" * 60)
    
    expert = SystemeExpert()
    
    print("\n--- Adding Rules ---")
    expert.ajouteRegle(["rain"], "take_umbrella")
    expert.ajouteRegle(["cold"], "wear_jacket")
    expert.ajouteRegle(["take_umbrella", "wear_jacket"], "ready_to_go_out")
    expert.ajouteRegle(["snow"], "stay_home")
    
    print("\n--- Display Rules ---")
    expert.afficheRegles()
    
    print("\n--- Running Forward Chaining ---")
    expert.chainageAvantSimple(["rain", "cold"])
    
    expert.trace()
    
    print("\n--- Final Facts ---")
    expert.afficheFaits()
    
    print("\n--- Testing Clear Databases ---")
    expert.initDBs()
    expert.afficheFaits()
    expert.afficheRegles()
