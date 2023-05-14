import json


class Tokenizer:
    def __init__(self):
        json_file = 'SELFIES_Tokens.json'
        with open(json_file, 'r') as file:
            self.mapping = json.load(file)

        self.inverse_mapping = {v: k for k, v in self.mapping.items()}
        self.sorted_keys = sorted(self.mapping.keys(), key=len, reverse=True)

    def encode(self, input_string):
        encoded_string = ''
        cursor = 0
        while cursor < len(input_string):
            found = False
            for key in self.sorted_keys:
                if input_string[cursor:].startswith(key):
                    if encoded_string != '':
                        encoded_string += ' '  # add space as separator
                    # append encoded value
                    encoded_string += str(self.mapping[key])
                    cursor += len(key)
                    found = True
                    break
            if not found:
                raise ValueError(
                    f"Token not found in the dictionary: {input_string[cursor:]}")
        return encoded_string

    def decode(self, encoded_string):
        decoded_string = ''
        # split input string by space to get encoded list
        encoded_list = encoded_string.split(' ')
        for num in encoded_list:
            # decode each token
            decoded_string += self.inverse_mapping[int(num)]
        return decoded_string


# Usage
encoder = Tokenizer()
encoded = encoder.encode(
    '[SeH0R1][:0chiral][C][C][=N][N][=C][Branch2][Ring1][#Branch1][S][C][Branch1][C][C][C][Br][=Branch1][C][=O][N][C][=C][C][Branch1][C][Cl][=C][C][=C][Ring1][#Branch1][Cl][N][Ring2][Ring1][Ring1][N]')
print("Encoded:", encoded)
decoded = encoder.decode(encoded)
print("Decoded:", decoded)
