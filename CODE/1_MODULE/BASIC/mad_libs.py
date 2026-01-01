def mad_lib_creator(noun, verb, adjective):
    mad_lib =f"I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after {verb}ing a {adjective} {noun}. In the forest, there are {adjective} {noun}s and trees that can {verb}! I fall asleep each night on a {noun} of {noun}s and dream of {adjective} {noun}s. It feels as though I have lived here for many {noun}s."
    print(mad_lib)

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

mad_lib_creator(noun,verb,adjective)
