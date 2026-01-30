raw_input = ' My Project Backup '

bucket_name = raw_input.strip()
bucket_name = bucket_name.replace(' ','-').lower()
print(bucket_name)
