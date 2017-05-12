import os
def rename_fils():
	file_names = os.listdir(r"/Users/yuwang/Desktop/daily notes/prank")
	path_save = os.getcwd()
	print(path_save)
	os.chdir(r"/Users/yuwang/Desktop/daily notes/prank")
	print(os.getcwd())
	print(file_names)
	for file in file_names:
		os.rename(file, file.translate(None, "0123456789"))
	os.chdir(path_save)
rename_fils()