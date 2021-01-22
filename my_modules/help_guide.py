class Helper:
    print('Enter "EXIT" to quit the tutorial at any time.')
    question = input(
        """Please enter any of the FOLLOWING TERMS to learn about how they fit into gameplay:
    *JAMMER
    *NODES
    *SONAR
    """
    )
    if "jam" in input.lower():
        print(
            """The JAMMER is the system software that is trying to prevent you from reaching the NEXUS NODE.
        There are TWO WAYS that you can be jammed:

        1) FAILING A NODE ENTRY:
                -- Every time you hack a node, you will have to press 'ENTER' within a certain range.
                if you fail this by pressing ENTER too late or too early, the JAMMER will trigger.

        2) FAILING A COUNTERMEASURE TEST:

                --If you enter a node that is within a randomly-selected JAMMER RANGE, you will be
                faced with a challenge of variable difficulty, where you must complete one of three
                types of test:
                *** Mathematics, where you must answer arithmetic questions correctly to progress
                *** System Commands, where you must type commands in the terminal
                *** DDOS Attacks, where you must type the 'i' key a certain number of times before pressing ENTER.

                Countermeasure tests only active if you select a NODE in the JAMMER RANGE.

        If you trigger the jammer, you will lose one HIGH or LOW entry randomly if you have the same amount of both,
        or lose ONE of the ENTRY TYPE you currently have more of.
        """
        )
