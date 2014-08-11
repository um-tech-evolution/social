class GoalInnovations:
    '''
    Maintains list of all possible successful recombinations and the
    compositions that form them.
    '''
    pass

class Tribe:
    '''
    A list of tribe members, technologies common to the tribe,
    technological goals, resources available to the tribe... Methods for
    movement, cohesion (members of a tribe inhabiting the same general
    area), resource use, adding and deleting tribe members.
    '''

    def __init__(self, tribeMemberList, technologyList, groupResource, goals):
        self.tribeMemberList = []
        self.technologyList = []
        self.groupsResource = []
    
    def addTribeMember(self, Agent):
        '''
        If an agent reproduces, add one agent to 'TribeMemberList.'
        '''
        pass

    def deleteTribeMember(self, agent):
        ''' 
        If an agent dies delete that agent from 'TribeMemberList.'
        '''
        pass

    def movement(self, agent):
        ''' 
        A method allowing agents of the same tribe to move similarly across the grid.
        '''
        pass
    
    def cohesion(self, agent):
        ''' 
        A method that causes agents of the same tribe to occupy the same general grid space.
        '''
        pass

    def resourceUseRate(self, agent, landscape):
        ''' 
        A method allowing agents of the same tribe to use resources at the same rate as other tribal members.
        '''
        pass

class Agent:
    '''
    A class that defines methods for communication and exchange between agents
    of different tribes. Aggregates Tribe. Maintains a list of technologies
    possessed by the agent that are available for exchange.
    '''
    
    def __init__(self, tribe):
        self.tribeStatus = tribe
        self.culturalKnowledge = [] + TechnologyList
    
    def communication(self, agent):
        '''
        Stop moving if an agent from another tribe is within a certain range on
        the grid space. Conditionally override the tribe's movement method.
        ''' 
        pass

    def exchange(self):
        ''' 
        Randomly select an item (code string) from each agent's
        `CulturalKnowledge`. Copy it and add to the other agent's
        `CulturalKnowledge`. Iterate over the list and remove duplicates.   
        '''    
        pass

class Innovator(Agent):
    '''
    A sub-class of agents able to form innovations from the process of cultural
    exchange.
    '''

    def __init__(self):
        super().__init__()

    def attemptInnovation(self, goalInnovations):
        '''
        After exchange occurs iterate over 'CulturalKnowledge,' look for
        matches in 'GoalInnovations.'
        '''
        pass

    def innovate(self, technologyList):
        ''' 
        Add successful recombinations to 'TechnologyList.' This should give
        some benefit to all agent's of the tribe, perhaps a decrease in the
        rate at which a resource is used up.
        '''
        pass
