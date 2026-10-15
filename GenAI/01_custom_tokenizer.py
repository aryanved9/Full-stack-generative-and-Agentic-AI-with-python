import tiktoken

enc = tiktoken.encoding_for_model('gpt-4o')
text = 'Hey, there my name is Aryan'
tokens = enc.encode(text)
print(f"encoded Tokens = {tokens}")

#  Output tokens = [25216, 11, 1354, 922, 1308, 382, 107851, 270]

decoded_tokens = enc.decode([25216, 11, 1354, 922, 1308, 382, 107851, 270])
print(f"Dcoded token = {decoded_tokens}")
