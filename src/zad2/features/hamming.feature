Feature: Hamming distance calculator
    

    Scenario: Two strands which are equal result in a distance of 0
        Given strand1 is ABB
        And strand2 is ABB
        When we calculate the distance
        Then the result is 0

    Scenario: Two strands which are empty result in a distance of 0
        Given strand1 is empty
        And strand2 is empty
        When we calculate the distance
        Then the result is 0

    Scenario: Two strands which have a different last letter result in a distance of 1
        Given strand1 is ABB
        And strand2 is ABC
        When we calculate the distance
        Then the result is 1

    Scenario: Two strands which are completely different result in a distance equal to their length
        Given strand1 is XYZ
        And strand2 is ABC
        When we calculate the distance
        Then the result is 3

    Scenario: When the second strand is longer than the first there is an error
        Given strand1 is XYZ
        And strand2 is ABCDEFG
        When we calculate the distance
        Then the program raises an error

    Scenario: When the second strand is shorter than the first there is an error
        Given strand1 is ABCDEFGHRETR
        And strand2 is ABC
        When we calculate the distance
        Then the program raises an error

    Scenario: first strand is ATGATA and the second is AGTTTA, result is 3
        Given strand1 is ATGATA
        And strand2 is AGTTTA
        When we calculate the distance
        Then the result is 3

    Scenario: When one string is empty there is an error
        Given strand1 is XYZ
        And strand2 is empty
        When we calculate the distance
        Then the program raises an error

