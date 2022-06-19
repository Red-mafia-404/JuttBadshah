import platform

arc = platform.uname().machine
if 'aarch' in arc:
	from jutbd import main
	main()
else:
	exit('machine not support!')
