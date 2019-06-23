import requests
from bs4 import BeautifulSoup


def cleanup(quote):
	import re
	MULTI_SPACE = '\s+'
	return re.sub(MULTI_SPACE, ' ', quote).strip()



def get_from_quotecatalog(page=1):
	BASE_URL = "https://quotecatalog.com/love/"
	URL = BASE_URL if page == 1 else BASE_URL + '{}/'.format(page)

	response = requests.get(URL)
	if response.status_code != 200:
		return list()

	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.select('.quote__text')
	quotes = [cleanup(q.text) for q in quotes]
	return quotes



if __name__ == '__main__':
	from functools import reduce
	from concurrent import futures


	with futures.ThreadPoolExecutor(max_workers=5) as ex:
		quotes = ex.map(get_from_quotecatalog, range(1, 101))
	quotes = reduce(lambda x, y: x + y, quotes)

	with open('../data/quotecatalog.txt', 'w') as f:
		f.write('\n'.join(quotes))





# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
# 			'Host': 'www.goodreads.com',
# 			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 			'Accept-Encoding': 'gzip, deflate, br',
# 			'Cache-Control': 'max-age=0',
# 			'Referer': 'https://www.google.com/',
# 			'Upgrade-Insecure-Requests': '1',
# 			'If-None-Match': 'W/"36cf4d70e0792f8014ff2f6abbd30099"',
# 			'connection': 'keep-alive',
# 			'Cookie': 'csid=BAhJIhg1NDctNjgyMDIwNS04ODA3MDI5BjoGRVQ%3D--54c94519f0586158c143eb5e7e241f25110064ba; locale=en; csm-sid=162-6169738-9208214; _session_id2=87fb7b26f28ef84fe6c5a23e58734c6d; never_show_interstitial=true'}
