import requests, time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


url = "10.10.10.10/hello"

def requests_retry_session(
    retries=1,
    backoff_factor=0.01,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

s = requests.Session()
s.headers.update({'hello':'world'})

t0 = time.time()
try:
    response = requests_retry_session(session=s).get('http://127.0.0.1:5000/', timeout=0.2)
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')