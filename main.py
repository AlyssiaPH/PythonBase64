import decode_encode.decode
import decode_encode.encode

if __name__ == '__main__':
    print("Press one of the keys below to start an action")
    user_input = ''

    while user_input.lower() not in ('q', "quit"):
        user_input = input("Encode [E] | Decode [D] | Encode and Decode [ED] | Decode and Encode [DE]")

        if user_input.lower() in ("e", "encode"):
            decode_encode.encode.run("")
        elif user_input.lower() in ("d", "decode"):
            decode_encode.decode.run("")
        elif user_input.lower() in ("ed", "encode decode"):
            result = decode_encode.encode.run("")
            decode_encode.decode.run(result)
        elif user_input.lower() in ("de", "decode encode"):
            result = decode_encode.decode.run("")
            decode_encode.encode.run(result)
        else:
            pass