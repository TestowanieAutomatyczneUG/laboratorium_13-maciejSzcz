from behave import *
from src.zad1.friendships import Friendships

use_step_matcher("re")


@given("there are friend1 and friend2 and Friendships")
def step_impl(context):
    context.friendships = Friendships()
    context.friend1 = "Andrzej"
    context.friend2 = "Michal"


@given("there are friend1, friend2 and friend3 and Friendships")
def step_impl(context):
    context.friendships = Friendships()
    context.friend1 = "Andrzej"
    context.friend2 = "Michal"
    context.friend3 = "Mateusz"


@when("friend1 adds friends2")
def step_impl(context):
    context.friendships.make_friends(context.friend1, context.friend2)

@when("checking if friend1 is a friend of friend2")
def step_impl(context):
    context.are_friends = context.friendships.are_friends(context.friend1, context.friend2)

@when("friend1 adds friend2 and friend3")
def step_impl(context):
    context.friendships.make_friends(context.friend1, context.friend2)
    context.friendships.make_friends(context.friend1, context.friend3)

@when("friend1 adds friend2 as friend, but friend2 doesn't add friend1")
def step_impl(context):
    context.friendships.add_friend(context.friend1, context.friend2)
    context.friendships.add_friend(context.friend2, None)

@then("friend2 is in friends1 friendslist")
def step_impl(context):
    assert context.friendships.get_friends_list(context.friend1) == [context.friend2]

@then("friend1 is in friends2 friendslist")
def step_impl(context):
    assert context.friendships.get_friends_list(context.friend2) == [context.friend1]

@then("friend1 and friend2 are friends")
def step_impl(context):
    assert context.friendships.are_friends(context.friend2, context.friend1)

@then("the result is false")
def step_impl(context):
    assert context.are_friends == False

@then("friend1 has two friends")
def step_impl(context):
    assert len(context.friendships.get_friends_list(context.friend1)) == 2


@then("friend1 is not in friends2 friendship list, but he is in friends1 list")
def step_impl(context):
    assert context.friendships.get_friends_list(context.friend1) == [context.friend2]
    assert context.friendships.get_friends_list(context.friend2) == [None]

