names = ['John', 'Jane', 'Doe', 'Alice', 'Bob']
scores = [85, 92, 78, 90, 88]
print(f'{"Name":<10} {"Score":<5}')
print("-" * 15)
for name, score in zip(names, scores):
    print(f"{name:<10} {score:<5}")