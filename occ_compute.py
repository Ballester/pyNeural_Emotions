#Class to receive environment information packages and transform into an external input package

#environment_status is a list composed of:
'''
[0] -> magnitude
[1] -> events, agents or objects
[2] -> pleased, displeased, approving, disapproving, liking, disliking
[3] -> c_others, c_self, s_agent, o_agent
[4] -> d_other, ud_other, p_relevant, p_irrelevant

'''

from Feeling import Feelings


class OCC:
    
    def __init__(self, external_deviation, update_deviation):
        self.external_dev = external_deviation
        self.update_dev = update_deviation
        self.compute_list = []

    def performInput(self, nodes):
        if len(self.compute_list) > 0:
            loop = len(self.compute_list)
            for i in xrange(loop):
                environment_status = self.compute_list.pop(0)
                return transform(environment_status, nodes)
                
        else:
            return False
        
    def transform(self, environment_status, nodes):
        if environment_status[1] == "events":

            if environment_status[2] == "pleased":
                if environment_status[3] == "c_others":
                    if environment_status[4] == "d_others":
                        return self.finalTransform(("happy-for","resentment"), nodes)
                    
                    elif environment_status[4] == "ud_other":
                        return self.finalTransform(("gloating","pity"), nodes)

                    else:
                        raise NameError('Invalid OCC_package')


                elif environment_status[3] == "c_self":
                    if environment_status[4] == "p_relevant":
                        return self.finalTransform(("hope","fear"), nodes)

                    elif environment_status[4] == "p_irrelevant":
                        return self.finalTransform(("joy","distress"), nodes)                        

                    else:
                        raise NameError('Invalid OCC_package')

                else:
                    raise NameError('Invalid OCC_package')          
            
            elif environment_status[2] == "displeased":
                if environment_status[3] == "c_others":
                    if environment_status[4] == "d_others":
                        return self.finalTransform(("resentment","happy-for"), nodes)

                    elif environment_status[4] == "ud_others":
                        return self.finalTransform(("pity","gloating"), nodes)                        

                    else:
                        raise NameError('Invalid OCC_package')

                
                elif environment_status[3] == "c_self":
                    if environment_status[4] == "p_relevant":
                        return self.finalTransform(("fear","hope"), nodes)

                    elif environment_status[4] == "p_irrelevant":
                        return self.finalTransform(("distress","joy"), nodes)

                    else:
                        raise NameError('Invalid OCC_package')


                else:
                    raise NameError('Invalid OCC_package')

            else:
                raise NameError('Invalid OCC_package')
        
        elif environment_status[1] == "agents":
            if environment_status[2] == "approving":
                if environment_status[3] == "s_agent":
                    return self.finalTransform(("pride","shame"), nodes)                

                elif environment_status[3] == "o_agent":
                    return self.finalTransform(("admiration","reproach"), nodes)

                else:
                    raise NameError('Invalid OCC_package')

            elif environment_status[2] == "disapproving":
                if environment_status[3] == "s_agent":
                    return self.finalTransform(("shame","pride"), nodes)

                elif environment_status[3] == "o_agent":
                    return self.finalTransform(("reproach","admiration"), nodes)
    
                else:
                    raise NameError('Invalid OCC_package')



            else:
                raise NameError('Invalid OCC_package')

        elif environment_status[1] == "objects":
            if environment_status[2] == "liking":
                return self.finalTransform(("joy","distress"), nodes)

            elif environment_status[2] == "disliking":
                return self.finalTransform(("distress","joy"), nodes)

            else:
                raise NameError('Invalid OCC_package')

        else:
            raise NameError('Invalid OCC_package')


    def finalTransform(self, final_input, nodes):
        feelings.compute(self.external_dev, self.update_dev, nodes, final_input, environment_status[0])








