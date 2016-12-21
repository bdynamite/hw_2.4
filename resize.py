import subprocess
import os
import glob

app = 'convert.exe'
input_dir = 'source'
output_dir = 'result'

def get_files(directory):
	return glob.glob(os.path.join(directory, "*.jpg"))

def quantity():
	if len(files) >= 4:
		return 4
	else:
		return len(files) 

files = get_files(input_dir)

try:
	os.mkdir(os.path.join(output_dir))
except Exception as e:
	None
       #, mode=0o777, *, dir_fd=None)

while files:
	pipes = []
	for i in range(quantity()):
		cmd = ' '.join((app, files[0], '-resize 200', files[0].replace(input_dir, output_dir)))
		pipe = subprocess.Popen(cmd, shell = True)
		pipes.append(pipe)
		files.remove(files[0])
	while pipes:
		pipe = pipes.pop()
		pipe.wait()

print("process finished")
