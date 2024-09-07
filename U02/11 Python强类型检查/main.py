def greet(name: str) -> str:
    return f"Hello, {name}!"

# 正确使用
print(greet("Alice"))

# 错误使用
print(greet(123))  # 运行时不会报错，但类型检查工具会提示错误

result = greet("Alice")
result += 1
print(result)