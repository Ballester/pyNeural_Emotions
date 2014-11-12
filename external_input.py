from occ_compute import OCC

class ExternalInput:
    
    def __init__(self, external_deviation, update_deviation):
        self.occ = OCC(external_deviation, update_deviation)
        self.ext_dev = external_deviation
        self.up_dev = update_deviation
        self.file_counter = 0
        self.last_input = []
        
    def checkForExternalInput(self):
        try:
            fid = open("externals/external_file_" + str(self.file_counter) + ".in")
            self.last_input = fid.readline()
            self.last_input = self.last_input.split()
            self.file_counter += 1
            self.occ.compute_list.append(self.last_input)
            return True
            
        except:
            return False
        
    def performExternalInputs(self, nodes):    
        self.occ.performInput(nodes)
    
