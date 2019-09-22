import string

def most_frequent(s):
	d = dict()
	inv = dict()
	for char in s:
		if char in string.ascii_letters:
			letter = char.lower()		
			d[letter] = d.get(letter, 0) + 1
			
	for letter, freq in d.items():
		inv.setdefault(freq, []).append(letter)
		
	for freq in sorted(inv, reverse=True):
		print('{:.2%}:'.format(freq/(sum(list(inv)*len(inv[freq])))), ', '.join(inv[freq]))
