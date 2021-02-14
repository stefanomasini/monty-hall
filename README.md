# monty-hall
Month Hall Problem

https://en.wikipedia.org/wiki/Monty_Hall_problem

With a simple software simulation, this normally counter-intuitive problem becomes more obvious:

    def no_switch_behaviour():
        doors = [True, False, False]
        shuffle(doors)
        return doors[0]
    
    
    def switch_behaviour():
        doors = [True, False, False]
        shuffle(doors)
        if not doors[2]:
            return doors[1]
        else:
            return doors[2]

Output of the program:

    NO SWITCH: Success rate 33.26%
    SWITCH: Success rate 66.62%

You can see that the behaviour of never switching the original choice is basically equivalent to randomly 
choosing one out of 3 doors, i.e. 1/3.

The switching behaviour, on the other hand, is basically peeking behind the last door and explicitly excluding 
it from the choices if it's not the right one. So there are 2 cases:

1. The last door is not the good one (2/3 probability), so show it and the switch. In that case the probability 
   of picking the right one after the switch is 1/2.
2. The last door is the good one (1/3 probability). In that case, the bad door being shown is the second one, 
   and the switch will necessarily land on the good one, i.e. the third.

The probability of picking the right door in scenario 1 is 2/3 * 1/2 = 1/3. The probability of scenario 2 is 1/3, 
so overall probability of choosing the right door is 1/3+1/3 = 2/3.

Q.E.D. :-)
