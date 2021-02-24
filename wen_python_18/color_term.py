import tqdm, random, time

progresBar = tqdm.tqdm(range(0, 100), desc='Loading virus...', ascii=True, bar_format='{desc}: {bar} {percentage:3.0f}% ')
for x in progresBar: 
	time.sleep(.05)
