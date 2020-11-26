default_ElectronCoordinateShell1 = [[0, 75], [0, -75]];
default_ElectronCoordinateShell2 = [[115.5, 48], [47.8, 115.5], [115.5, -48], [47.8, -115.5], [-115.5, 48], [-47.8, 115.5], [-115.5, -48], [-47.8, -115.5]];
default_ElectronCoordinateShell3 = [[175, 0], [-175, 0]];

class Atom:
    def __init__ (self, anzShells, anzElectronShell1, anzElectronShell2, anzElectronShell3):
        self.anzShells = anzShells;
        self.anzElectronShell1 = anzElectronShell1;
        self.anzElectronShell2 = anzElectronShell2;
        self.anzElectronShell3 = anzElectronShell3;
        
    
    def getAllElectronCoordinate(self):
        allElectronCoordinate = [];
        for atomNr in range(0, self.anzElectronShell1):   
            allElectronCoordinate.append(default_ElectronCoordinateShell1[atomNr])
        for atomNr in range(0, self.anzElectronShell2):    
            allElectronCoordinate.append(default_ElectronCoordinateShell2[atomNr])
        for atomNr in range(0, self.anzElectronShell3):    
            allElectronCoordinate.append(default_ElectronCoordinateShell3[atomNr])
        return allElectronCoordinate;
    
