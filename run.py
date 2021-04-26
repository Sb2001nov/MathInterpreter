import core

while True:
    text = input('math >> ')
    result, error = core.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)