import random

def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word),word))
	t.sort(reverse=True)
	res = []
	for length, word in t:
		res.append(word)
	i=0
	final = []
	while i <= len(res)-2:
		if len(res[i]) == len(res[i+1]):
			y_list = [res[i], res[i+1]]
			random.shuffle(y_list)
			final = final + y_list
			i += 2
		else:
			final.append(res[i])
			i += 1
	if i == len(res)-1:
		final.append(res[i])
	return final
