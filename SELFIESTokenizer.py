import json


class SELFIESTokenizer:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.mapping = json.load(file)

        self.inverse_mapping = {v: k for k, v in self.mapping.items()}
        self.sorted_keys = sorted(self.mapping.keys(), key=len, reverse=True)

    def encode(self, input_string):
        encoded_list = []
        cursor = 0
        while cursor < len(input_string):
            found = False
            for key in self.sorted_keys:
                if input_string[cursor:].startswith(key):
                    encoded_list.append(self.mapping[key])
                    cursor += len(key)
                    found = True
                    break
            if not found:
                raise ValueError(
                    f"Token not found in the dictionary: {input_string[cursor:]}")
        return encoded_list

    def decode(self, encoded_list):
        decoded_string = ''
        for num in encoded_list:
            decoded_string += self.inverse_mapping[num]
        return decoded_string


# Usage
# encoder = SELFIESTokenizer('SELFIES_Tokens_Plus.json')
# encoded = encoder.encode(
#     '[SeH0R1][:0chiral][C][C][=N][N][=C][Branch2][Ring1][#Branch1][S][C][Branch1][C][C][C][Br][=Branch1][C][=O][N][C][=C][C][Branch1][C][Cl][=C][C][=C][Ring1][#Branch1][Cl][N][Ring2][Ring1][Ring1][N]')
# print("Encoded:", encoded)
# decoded = encoder.decode(encoded)
# print("Decoded:", decoded)
