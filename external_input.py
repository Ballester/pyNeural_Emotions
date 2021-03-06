from occ_compute import OCC

class ExternalInput:
    
    def __init__(self, external_deviation, update_deviation):
        self.occ = OCC(external_deviation, update_deviation)
        self.ext_dev = external_deviation
        self.up_dev = update_deviation
        self.file_counter = 0
        self.last_input = []
        self.fid = 0

    '''  
    Separated files:
   
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
    '''

    #Single file
    def checkForExternalInput(self):
        if self.file_counter == 0:
            self.file_counter += 1
            self.fid = open("externals/external_single_file.in")
            return self.getInput()    

        else:
            return self.getInput()


    def getInput(self):
        try:
            self.last_input = self.fid.readline()
            self.last_input = self.last_input.split()
            self.occ.compute_list.append(self.last_input)
            if len(self.last_input) == 0:
                return False
            else:
                return True
        
        except:
            return False

    
    def performExternalInputs(self, nodes):    
        self.occ.performInput(nodes)
    
