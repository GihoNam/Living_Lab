import Xlsx             #Excel Save
import Simple_server   #TCP Socket


data = Simple_server.Setting('127.0.0.1',8888)
data = data.split(",")
print(data)




