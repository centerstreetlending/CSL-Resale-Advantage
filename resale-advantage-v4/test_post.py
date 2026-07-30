import urllib.request
import urllib.parse

url = 'https://docs.google.com/forms/d/e/1FAIpQLSfhmb86XIYUTqYeA531lC3j4WxLtnye4eh3dgd1JKC9rWcIXg/formResponse'
data = {
    'entry.1281752874': 'TestFirst',
    'entry.511625773': 'TestLast',
    'entry.1714112113': 'test@example.com',
    'entry.1515225399': '555-555-5555',
    'entry.289374821': "I'm ready to list now",
    'entry.1894957803': "Yes — send me details about the program",
    'entry.2092099687': "I agree that Center Street Lending and its affiliates may contact me about the Investor Exit Advantage program by phone, email, or text at the information provided. Consent is not a condition of any loan. (Pending legal review.)"
}

data = urllib.parse.urlencode(data).encode()
req = urllib.request.Request(url, data=data)
try:
    response = urllib.request.urlopen(req)
    print(response.getcode())
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode())
