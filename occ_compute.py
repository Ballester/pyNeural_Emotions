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
    
    def __init__(self):
        self.compute_list = []

    def checkInput(self):
        if len(compute_list > 0):
            environment_status = self.compute_list.pop(0)
            return transform(environment_status)
        
    def transform(self, environment_status):
        if environment_status[1] == "events":

            if environment_status[2] == "pleased":
                if environment_status[3] == "c_others":
                    if environment_status[4] == "d_others":
                        return self.finalTransform("happy-for")
                    
                    elif environment_status[4] == "ud_other":
                        return self.finalTransform("gloating")

                    else:
                        raise NameError('Invalid OCC_package')


                elif environment_status[3] == "c_self":
                    if environment_status[4] == "p_relevant":
                        return self.finalTransform("hope")

                    elif environment_status[4] == "p_irrelevant":
                        return self.finalTransform("joy")                        

                    else:
                        raise NameError('Invalid OCC_package')

                else:
                    raise NameError('Invalid OCC_package')          
            
            elif environment_status[2] == "displeased":
                if environment_status[3] == "c_others":
                    if environment_status[4] == "d_others":
                        return self.finalTransform("resentment")

                    elif environment_status[4] == "ud_others":
                        return self.finalTransform("pity")                        

                    else:
                        raise NameError('Invalid OCC_package')

                
                elif environment_status[3] == "c_self":
                    if environment_status[4] == "p_relevant":
                        return self.finalTransform("fear")

                    elif environment_status[4] == "p_irrelevant":
                        return self.finalTransform("distress")

                    else:
                        raise NameError('Invalid OCC_package')


                else:
                    raise NameError('Invalid OCC_package')

            else:
                raise NameError('Invalid OCC_package')
        
        elif environment_status[1] == "agents":
            if environment_status[2] == "approving":
                if environment_status[3] == "s_agent":
                    return self.finalTransform("pride")                

                elif environment_status[3] == "o_agent":
                    return self.finalTransform("admiration")

                else:
                    raise NameError('Invalid OCC_package')

            elif environment_status[2] == "disapproving":
                if environment_status[3] == "s_agent":
                    return self.finalTransform("shame")

                elif environment_status[3] == "o_agent":
                    return self.finalTransform("reproach")
    
                else:
                    raise NameError('Invalid OCC_package')



            else:
                raise NameError('Invalid OCC_package')

        elif environment_status[1] == "objects":
            if environment_status[2] == "liking":
                return self.finalTransform("joy")

            elif environment_status[2] == "disliking":
                return self.finalTransform("distress")

            else:
                raise NameError('Invalid OCC_package')

        else:
            raise NameError('Invalid OCC_package')


    def finalTransform(self, final_input):
        







