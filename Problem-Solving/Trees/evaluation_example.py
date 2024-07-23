import random


def read_dict(filename):
    dictionary = list()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            dictionary.append(line)
    return dictionary


def sample(dictionary):
    idx = random.randint(0, len(dictionary) - 1)
    return dictionary[idx]


def compute_response(target, guess):
    """
    Given the hidden word and a guess, return a string representing whether the letters are correct (and in the correct
    place)
    :param target: the hidden word
    :param guess: the guess the user has just made
    :return: a string indicating how correct they are (see Task 5)
    """
    pass  # you would need to fill this in with code you did in task 5.



def play_round(words, target, max_guesses=6):

    previous_guesses = list()
    previous_feedback = list()
    for guess_id in range(1, max_guesses + 1):
        guess = make_new_guess(words, previous_guesses, previous_feedback)  # this is what you would be implementing
        feedback = compute_response(target, guess)
        if feedback == target:
            # winner!
            return guess_id
        previous_guesses.append(guess)
        previous_feedback.append(feedback)
    return max_guesses


def make_new_guess(words, previous_guesses, previous_feedback):
    """
    This is the function you submit
    """
    return "HELLO"


if __name__ == '__main__':

    words = read_dict('dict.txt')
    seed = 42
    random.seed(seed)

    max_guess = 6
    num_runs = 10
    target_words = [sample(words) for _ in range(num_runs)]

    total_guesses = 0
    for round in range(num_runs):
        num_guesses = play_round(words, target_words[round], max_guess)
        total_guesses += num_guesses
    print(total_guesses / num_runs)
