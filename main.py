from decode_encode.decode import run as decode
from decode_encode.encode import run as encode

if __name__ == '__main__':
    print("Press one of the keys below to start an action")
    user_input = ''

    while user_input.lower() not in ('q', "quit"):
        user_input = input("Encode [E] | Decode [D] | Encode and Decode [ED] | Decode and Encode [DE]")

        if user_input.lower() in ("e", "encode"):
            encode("")
        elif user_input.lower() in ("d", "decode"):
            decode("")
        elif user_input.lower() in ("ed", "encode decode"):
            result = encode("")
            decode(result)
        elif user_input.lower() in ("de", "decode encode"):
            result = decode("")
            encode(result)
        else:
            pass