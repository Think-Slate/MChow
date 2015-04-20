import pycurl, random, datetime
from cStringIO import StringIO

bowl_id = 5500

def random_date():
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    end = datetime.datetime.now()
    start = datetime.datetime.now().replace(month=datetime.datetime.now().month - 1)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

# @app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>/<date_time>')
for i in range(0, 100):
	c = pycurl.Curl()
	water_fill = random.uniform(0, 1000)
	food_fill = random.uniform(0, 200)
	url = 'http://mchow.herokuapp.com/petinfo/' + str(bowl_id) + '/' + str(water_fill) + '/' + str(food_fill) + '/' + str(random_date()).replace(" ", "%")
	print url
	c.setopt(pycurl.URL, url)
	c.perform()
	c.close()

# SELECT_TIMEOUT = 1.0
# num_handles = len(reqs)
# while num_handles:
# 	ret = m.select(SELECT_TIMEOUT)
# 	if ret == -1:
# 		continue
# 	while 1:
# 		ret, num_handles = m.perform()
# 		if ret != pycurl.E_CALL_MULTI_PERFORM: 
# 			break
	
# for req in reqs:
#     print req[1].getvalue()
