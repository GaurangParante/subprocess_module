import subprocess as sp

# sp.run()

# result = sp.run("echo gauramg",shell=True,capture_output=True,text=True)
# print(result.stdout)

# sp.Popen()
# process = sp.Popen(['ping','google.com','-n','4'],stdout=sp.PIPE,text=True)

# for line in process.stdout:
#     print(line.strip())

output = sp.check_output('echo python rocks!!',shell=True,text=True)
print(output)