import Algorithmia
from six.moves import input

# TODO: Replace this with your api key on https://algorithmia.com/
api_key = "<YOUR API KEY>"


def autocomplete(algo, code):
    "Returns first 10 next word results"
    return algo.pipe(code).result


def autocomplete_sequence(algo, code, num_tokens, num_results=1):
    "Returns auto complete result with num_tokens"
    options = {'code': code, 'num_tokens': num_tokens, 'num_results': num_results}
    return algo.pipe(options).result

if __name__ == '__main__':
    # Ask for API key if needed
    if api_key == '<YOUR API KEY>':
        api_key = input('Algorithmia API key:')
    client = Algorithmia.client(api_key)
    algo = client.algo('PetiteProgrammer/pythoncodeprediction/1.0.3')

    while True:
        code = input('>')
        suggestion = autocomplete_sequence(algo, code, 5)
        print([' '.join(tokens) for tokens in suggestion][0])
