from threading import Thread
import os
import time


result = None


def normalize_num(number: int):
	if len(str(number)) == 1:
		return "0" + str(number)
	else:
		return str(number)


def run_test(file_name: str, test_path: str, lang: str):
	try:
		ans = os.popen(("./" if lang == 'c++' else "python3 ") + file_name + " < " + test_path).readlines()
	except FileNotFoundError:
		exit()
	right = open(test_path + ".a", 'r').readlines()
	global result
	result = ans == right


def run_task(file_name: str, testes_path: str, lang: str, time_limit: float):
	global result
	i = 1
	while True:
		if lang == "c++":
			os.system("g++ -std=c++17 -o "+os.getcwd()+"/solve "+os.getcwd()+"/"+file_name)
			task = Thread(target=run_test, args=("solve", testes_path+"/"+normalize_num(i), lang))
		else:
			task = Thread(target=run_test, args=(file_name, testes_path + "/" + normalize_num(i), lang))
		task.start()
		time.sleep(time_limit)
		task.stopped = True
		if result is None:
			print(str(i)+": "+"TL")
		else:
			if result:
				print(str(i) + ": " + "OK")
			else:
				print(str(i) + ": " + "WA")
		i += 1
		result = None


def main():
	lang = input("Exapmle: c++\nExample2: python\nEnter lang: ")
	file_name = input("Example: main.cpp\nEnter file name: ")
	testes_path = input("Example: /Users/ars/Desktop/v2020/a/tests\nEnter path to testes folder: ")
	time_limit = float(input("Example: 0.5\nEnter time limit: "))
	# lang = "c++"
	# file_name = "main.cpp"
	# testes_path = "/Users/ars/Desktop/v2020/a/tests"
	# time_limit = 1
	run_task(file_name, testes_path, lang, time_limit)


if __name__ == "__main__":
	main()