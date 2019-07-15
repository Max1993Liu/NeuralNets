import os
from PIL import Image
import numpy as np
import tqdm


label = ['angry', 'disgust' ,'fear' , 'happy', 'sad', 'surprise', 'neutral']

with open('./data/fer2013.csv', 'r') as f:
	f.readline()

	for i, line in enumerate(f.readlines()):
		label, img, usage = line.split(',')
		print(img)
		img = Image.fromarray(np.array([int(i) for i in img.split()]).reshape((48, 48)).astype('uint8'))

		outdir = './data/{}/{}'.format(usage.strip(), label.strip())
		
		try:
			os.makedirs(outdir)
		except:
			pass

		outpath = os.path.join(outdir, '{}.png'.format(i))
		img.save(outpath)


