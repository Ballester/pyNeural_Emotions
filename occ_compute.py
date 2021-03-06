#Class to receive environment information packages and transform into an external input package

#environment_status is a list composed of:
'''
[0] -> magnitude
[1] -> events, agents or objects
if events:
    [2] -> pleased, displeased
    [3] -> c_others, c_self
    [4] -> d_others, ud_others

if agents:
    [2] -> approving, disapproving
    [3] -> s_agent, o_agent
    [4] -> p_relevant, p_irrelevant

if objects:
    [2] -> liking, disliking
'''

from Feeling import Feelings

class OCC:
    
    def __init__(self, external_deviation, update_deviation):
        self.external_dev = external_deviation
        self.update_dev = update_deviation
        self.compute_list = []
        self.environment_status = []
        self.feelings = Feelings()

    def performInput(self, nodes):
        if len(self.compute_list) > 0:
            loop = len(self.compute_list)
            for i in xrange(loop):
                self.environment_status = self.compute_list.pop(0)
                return self.transform(nodes)
                
        else:
            return False
        
    def transform(self, nodes):
        if self.environment_status[1] == "events":

            if self.environment_status[2] == "pleased":
                if self.environment_status[3] == "c_others":
                    if self.environment_status[4] == "d_others":
                        return self.finalTransform(("Happy-for","Resentment"), nodes)
                    
                    elif self.environment_status[4] == "ud_others":
                        return self.finalTransform(("Gloating","Pity"), nodes)

                    else:
                        raise NameError('Invalid OCC_package')


                elif self.environment_status[3] == "c_self":
                    if self.environment_status[4] == "p_relevant":
                        return self.finalTransform(("Hope","Fear"), nodes)

                    elif self.environment_status[4] == "p_irrelevant":
                        return self.finalTransform(("Joy","Distress"), nodes)                        

                    else:
                        raise NameError('Invalid OCC_package')

                else:
                    raise NameError('Invalid OCC_package')          
            
            elif self.environment_status[2] == "displeased":
                if self.environment_status[3] == "c_others":
                    if self.environment_status[4] == "d_others":
                        return self.finalTransform(("Resentment","Happy-for"), nodes)

                    elif self.environment_status[4] == "ud_others":
                        return self.finalTransform(("Pity","Gloating"), nodes)                        

                    else:
                        raise NameError('Invalid OCC_package')

                
                elif self.environment_status[3] == "c_self":
                    if self.environment_status[4] == "p_relevant":
                        return self.finalTransform(("Fear","Hope"), nodes)

                    elif self.environment_status[4] == "p_irrelevant":
                        return self.finalTransform(("Distress","Joy"), nodes)

                    else:
                        raise NameError('Invalid OCC_package')


                else:
                    raise NameError('Invalid OCC_package')

            else:
                raise NameError('Invalid OCC_package')
        
        elif self.environment_status[1] == "agents":
            if self.environment_status[2] == "approving":
                if self.environment_status[3] == "s_agent":
                    return self.finalTransform(("Pride","Shame"), nodes)                

                elif self.environment_status[3] == "o_agent":
                    return self.finalTransform(("Admiration","Reproach"), nodes)

                else:
                    raise NameError('Invalid OCC_package')

            elif self.environment_status[2] == "disapproving":
                if self.environment_status[3] == "s_agent":
                    return self.finalTransform(("Shame","Pride"), nodes)

                elif self.environment_status[3] == "o_agent":
                    return self.finalTransform(("Reproach","Admiration"), nodes)
    
                else:
                    raise NameError('Invalid OCC_package')



            else:
                raise NameError('Invalid OCC_package')

        elif self.environment_status[1] == "objects":
            if self.environment_status[2] == "liking":
                return self.finalTransform(("Joy","Distress"), nodes)

            elif self.environment_status[2] == "disliking":
                return self.finalTransform(("Distress","Joy"), nodes)

            else:
                raise NameError('Invalid OCC_package')

        else:
            raise NameError('Invalid OCC_package')


    def finalTransform(self, final_input, nodes):
        self.feelings.compute(self.external_dev, self.update_dev, nodes, final_input, self.environment_status[0])








