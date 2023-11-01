from search import *

class WolfGoatCabbage(Problem):

    #fix initial
    def __init__(self, initial=frozenset({'F', 'G', 'W', 'C'}), goal = set()):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def goal_test(self, state):
        #returns True if the given state is a goal state
        return state == self.goal
    
    def result(self, state, action):
        #returns the new state reached from the given state 
        #and the given action. Assume that the action is valid.

        new_state = frozenset(state)
        
        if 'F' in state:
            new_state = new_state.difference(action)
        elif 'F' not in state:
            new_state = new_state.union(action)

       
        return frozenset(new_state)

    def actions(self, state):
        # returns a list of valid actions in the given state

        valid_actions = []
        moves = [{'F'},{'F', 'C'},{'F', 'W'},{'F', 'G'}]
     
        for move in moves: 
            new_state = self.result(state, move)           
            if 'F' not in new_state:
                if 'G' in new_state and 'C' in new_state and 'W' not in new_state:
                    continue
                if 'W' in new_state and 'G' in new_state and 'C' not in new_state:
                    continue
                if 'W' in new_state and 'G' in new_state and 'C' in new_state:
                    continue
            if 'F' in new_state:
                if 'W' in new_state and 'G' not in new_state and 'C' not in new_state:
                    continue
                if 'C' in new_state and 'G' not in new_state and 'W' not in new_state:
                    continue
            valid_actions.append(move)

        return valid_actions        


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)