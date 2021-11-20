import random
choices = ['Rock', 'Scissors', 'Paper']
scores = [0, 0]


def register_score(result):
    if result == 1:
        scores[0] += 1
    if result == -1:
        scores[1] += 1


def show_user_options():
    print(
        f"{pound_wrapped_text('#'*50)}\n{pound_wrapped_text(' CHOOSE ONE ')}\n1: {choices[0]}\n2: {choices[1]}\n3: {choices[2]}\n")


def get_computer_choice():
    return random.randint(0, 2)


def compare(user, computer):
    if user == computer:
        return 0
    if user == 0 and computer == 2:
        return -1
    if user == 2 and computer == 0:
        return 1
    if user < computer:
        return 1
    return -1


def show_round_choices(user, computer):
    print("{0}\nUser choice:\t{1}\nCPU choice:\t{2}".format(pound_wrapped_text(" CHOICES "),
                                                            choices[user], choices[computer]))


def pound_wrapped_text(text):
    side = '#'*((30-len(text))//2)
    return f"{side}{text}{side}"


def show_scores():
    print(
        f"{pound_wrapped_text(' SCOREBOARD ')}\nUser:\t{scores[0]}\nCPU:\t{scores[1]}")


def show_round_outcome(outcome):
    print(pound_wrapped_text(" OUTCOME "))
    if outcome == -1:
        print("Computer wins!")
    if outcome == 0:
        print("Draw!")
    if outcome == 1:
        print("User wins!")


def game_loop():
    while True:
        show_user_options()
        user_input = input()
        if user_input not in "123":
            break
        computer = get_computer_choice()
        user = int(user_input) - 1
        show_round_choices(user, computer)
        result = compare(user, computer)
        show_round_outcome(result)
        register_score(result)
        show_scores()
