import json

# 反序列化： sample.json -> python
with open('sample.json') as f:
    sample = json.load(f)

new_sample = {}
new_sample['id'] = sample['id']
new_sample['synchronous'] = sample['synchronous']
new_sample['status'] = sample['status']
new_sample['actions'] = sample['actions']
print(new_sample)

# 序列化： python -> new_sample.json
with open('new_sample.json', 'w') as f:
    json.dump(new_sample, f, indent=4)