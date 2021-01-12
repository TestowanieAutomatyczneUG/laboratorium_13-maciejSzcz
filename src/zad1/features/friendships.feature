Feature: Friendships
    

    Scenario: Friend 1 adds Friend 2
        Given there are friend1 and friend2 and Friendships
        When friend1 adds friends2
        Then friend2 is in friends1 friendslist
        And friend1 is in friends2 friendslist

    Scenario: Friend 1 adds Friend 2
        Given there are friend1 and friend2 and Friendships
        When friend1 adds friends2
        Then friend1 and friend2 are friends

    Scenario: Friend1 and friend2 are not friends, checking if they are friends
        Given there are friend1 and friend2 and Friendships
        When checking if friend1 is a friend of friend2
        Then the result is false

    Scenario: Friend 1 adds Friend 2 and Friend3
        Given there are friend1, friend2 and friend3 and Friendships
        When friend1 adds friend2 and friend3
        Then friend1 has two friends

    Scenario: There are no friends and we try to get friends
        Given there are friend1 and friend2 and Friendships
        When friend1 adds friend2 as friend, but friend2 doesn't add friend1
        Then friend1 is not in friends2 friendship list, but he is in friends1 list
