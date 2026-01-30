url = 'https://api.github.com/v3'

part = url.split('/')[2]

domain_name = part.split('api.')[1]

print(domain_name)