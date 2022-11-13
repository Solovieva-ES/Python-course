from pprint import pprint
dict_hex = [{'bin': bin(i),'oct': oct(i),'dec': (i),'hex': hex(i)} for i in range(16)]
pprint(dict_hex)
