raw_input_port = '8080'
port_int = int(raw_input_port)
# print(type(port_int))

if port_int >= 1 and port_int <= 65535 :
    print('Valid')
else:   
    print('Invalid')