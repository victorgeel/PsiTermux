#Compiled By Victor_Geek
import marshal
compiled_code = b"c\x00\x00\x00\x00\x00\x00\x>
#Decoding and executing the compiled code
exec(marshal.loads(compiled_code))
