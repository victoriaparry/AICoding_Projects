from search import *

class WolfGoatCabbage(Problem):

    #fix initial
    def __init__(self, initial=frozenset({'F', 'G', 'W', 'C'}), goal = frozenset()):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def goal_test(self, state):
        #returns True if the given state is a goal state
        return state == self.goal
    
    def result(self, state, action):
        #returns the new state reached from the given state 
        #and the given action. Assume that the action is valid.
        # new_state = state
        new_state = frozenset(i for i in state if i not in action) | frozenset(i for i in action if i not in state)
        # for i in action:
        #     if i in new_state:
        #         new_state.remove(i)     
        #     else:
        #         new_state.add(i)   
        return new_state

    def actions(self, state):
        # returns a list of valid actions in the given state
        # possible_moves = [['F'], ['F','W'], ['F','G'], ['F','C']]

        # if state == {'W', 'G', 'F', 'C'}:
        #     return [['F', 'G']]
        # if state == {'W', 'C'}:
        #     return [['F', 'G'], ['F']]
        # if state == {'W', 'C', 'F'}:
        #     return [['F'], ['F', 'W'], ['F','C']]
        # if state == {'C'}:
        #     return [['F', 'W'], ['F','G']]
        # if state == {'F', 'G', 'C'}:
        #     return [['F', 'C'], ['F', 'G']]
        # if state == {'W'}:
        #     return[['F', 'G'], ['F', 'C']]
        # if state == {'W', 'F', 'G'}:
        #     return [['F', 'W'], ['F','G']]
        # if state == {'G'}:
        #     return [['F'], ['F', 'W'], ['F','C']]
        # if state == {'G', 'F'}:
        #     return [['F'], ['F', 'G']]

        if state == frozenset({'W', 'G', 'F', 'C'}):
            return [['F', 'G']]
        if state == frozenset({'W', 'C'}):
            return [['F', 'G'], ['F']]
        if state == frozenset({'W', 'C', 'F'}):
            return [['F'], ['F', 'W'], ['F', 'C']]
        if state == frozenset({'C'}):
            return [['F', 'W'], ['F', 'G']]
        if state == frozenset({'F', 'G', 'C'}):
            return [['F', 'C'], ['F', 'G']]
        if state == frozenset({'W'}):
            return [['F', 'G'], ['F', 'C']]
        if state == frozenset({'W', 'F', 'G'}):
            return [['F', 'W'], ['F', 'G']]
        if state == frozenset({'G'}):
            return [['F'], ['F', 'W'], ['F', 'C']]
        if state == frozenset({'G', 'F'}):
            return [['F'], ['F', 'G']]
        
        

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)