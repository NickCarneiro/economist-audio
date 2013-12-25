from pyquery import PyQuery
from local import settings
import requests

print 'getting form_build_id'
# first we need to get a form_build_id from the login form html
r = requests.get('http://www.economist.com/audio-edition/latest')
cookies = r.cookies
html = r.text
q = PyQuery(html)
inputs = q('input[name="form_build_id"]')
form_build_id_input = inputs[0]
form_build_id = q(form_build_id_input).val()
print 'found it: {}'.format(form_build_id)
payload = {
    'name': settings['email_address'],
    'pass': settings['password'],
    'form_build_id': form_build_id,
    'form_id': 'user_login',
    'securelogin_original_baseurl': 'http://www.economist.com',
    'op': 'Log in'
}
headers = {
    'content-type': 'application/x-www-form-urlencoded'
}
print 'logging in'
r = requests.post('https://www.economist.com/audio-edition/latest',
                  cookies=cookies, data=payload, headers=headers)
html = r.text
print html
q = PyQuery(html)
download_span = q('.audio-issue-full-download-link')
if len(download_span) == 0:
    print 'failed to log in'
    exit(1)
else:
    #otherwise, we've got a download link.
    # get the link that's inside the span
    links = q(download_span).children()
    link = links[0]
    href = q(link).attr('href')
    print 'download link {}'.format(href)
