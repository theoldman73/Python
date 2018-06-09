import os
os.remove("demo1.txt")
import os
if os.path.exists("demo1.txt"):
	os.remove("demo1.txt")
else:
	print("The file does not exists")

