def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"


greeting = greet("hello, computer")
# greeting = greet("how's the weather?")

print("Hm, " + greeting + " David")
