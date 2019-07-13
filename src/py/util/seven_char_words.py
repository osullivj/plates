import json
import sys

def create_seven_char_dict( allpath, sevenp):
    with open( allpath, 'rt') as allf:
        all_dict = json.load( allf)
        seven_dict = dict( )
        for word, _ in all_dict.items( ):
            if len( word) < 8:
                seven_dict[word] = 1
        with open( sevenp, 'wt') as sevenf:
            json.dump( seven_dict, sevenf)

if __name__ == "__main__":
    create_seven_char_dict( sys.argv[1], sys.argv[2])
