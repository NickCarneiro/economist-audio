from ghost import Ghost
from local import settings

ghost = Ghost()
page, resources = ghost.open('http://www.economist.com/audio-edition/latest')

result, resources = ghost.fill("#user-login", {
    "name": settings['email_address'],
    "pass": settings['password']
})
print 'logging in'
page, resources = ghost.fire_on("#user-login", "submit", expect_loading=True)
download_url, resources = ghost.evaluate(
    "document.querySelector('.audio-issue-full-download-link > a').getAttribute('href');")

print 'download url {}'.format(download_url)
