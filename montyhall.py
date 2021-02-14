from random import shuffle


def no_switch_behaviour():
    doors = [True, False, False]
    shuffle(doors)
    return doors[0]


def switch_behaviour():
    doors = [True, False, False]
    shuffle(doors)
    if not doors[2]:
        # Show that the third door is not the good one, and then switch
        return doors[1]
    else:
        # If the third one is the good one, then the second one must not be, so show that one, and then switch.
        # But at that point, the switch will hit the good one for sure.
        return doors[2]


NUM_TESTS = 1000000
no_switch_num_successes = 0
switch_num_successes = 0
for i in range(NUM_TESTS):
    if no_switch_behaviour():
        no_switch_num_successes += 1
    if switch_behaviour():
        switch_num_successes += 1

print('NO SWITCH: Success rate {0:.2f}%'.format(no_switch_num_successes / NUM_TESTS * 100))
print('SWITCH: Success rate {0:.2f}%'.format(switch_num_successes / NUM_TESTS * 100))
