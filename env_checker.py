import os
user = os.environ.get('USER')
path = os.environ.get('PATH')

print(f"Current user: {user}")
print(f"Current path: {path}")

target_dir = os.path.expanduser('~/devops_journey')
if os.path.exists(target_dir):
    print(f"Directory found: {target_dir}")
else:
    print(f"Directory not found: {target_dir}")