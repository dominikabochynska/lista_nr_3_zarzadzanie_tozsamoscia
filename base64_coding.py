import base64

# encode
given_string = "Hello World"
#code message to ascii
byte_msg = given_string.encode('ascii')
# message to base64
base64_val = base64.b64encode(byte_msg)
# message format to print
print("The Converted value of the string " + given_string + " is " + str(base64_val))

# decode
base64_message = 'SGVsbG8gV29ybGQ='
#code message to ascii
base64_bytes = base64_message.encode('ascii')
# code message to base64
message_bytes = base64.b64decode(base64_bytes)
print("Decode message is " + str(message_bytes))


