import imp


class Gambusino:

    def __init__(self, iaName, iaSourcePath):
        self.ia = imp.load_source(iaName, iaSourcePath)


gambusinoA = Gambusino('ia01', 'ia01.py')
gambusinoB = Gambusino('ia02', 'ia02.py')
gambusinoC = Gambusino('ia01', 'ia01.py')
gambusinoD = Gambusino('ia02', 'ia02.py')
print gambusinoA.ia.description
print gambusinoB.ia.description
print gambusinoC.ia.description
print gambusinoD.ia.description
