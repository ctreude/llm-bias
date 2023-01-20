import deepl 
import numpy as np

translator = deepl.Translator("<API Token>") 

tasks = []
file_handle = open("tasks.txt")
for line in file_handle:
	tasks.append(line)

output = open("output.txt", "w")

for i in range(100):
	print(i)
	permutation = np.random.permutation(tasks)
	result = [[task.rstrip()] for task in permutation]
	original_text = "".join(permutation)
	finnish_result = translator.translate_text(original_text, target_lang="FI") 
	english_result = translator.translate_text(finnish_result.text, target_lang="EN-US")
	counter = 0
	for line in english_result.text.rstrip().split("\n"):
		result[counter].append(line)
		counter += 1
	output.writelines([str(result_line) + "\n" for result_line in result])

output.close()