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

        new_state = state
        
        if 'F' in state:
            new_state = new_state.difference(action)
        elif 'F' not in state:
            new_state = new_state.union(action)

       
        return frozenset(new_state)

    def actions(self, state):
        # returns a list of valid actions in the given state

        valid_actions = []
        moves = [{'F'},{'F', 'G'},{'F', 'W'},{'F', 'C'}]

        if state == self.initial:
            return [moves[1]]
     
        for move in moves:            
            if 'F' not in state:
                if 'G' in state and 'C' in state and 'W' not in state:
                    continue
                if 'W' in state and 'G' in state and 'C' not in state:
                    continue
                if 'W' in state and 'G' in state and 'C' in state:
                    continue
                if 'C' in state and 'G' not in state and 'W' not in state:
                    continue
            if 'F' in state:
                if 'W' in state and 'G' not in state and 'C' not in state:
                    continue
            valid_actions.append(move)


        return valid_actions        


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)