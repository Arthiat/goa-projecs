def მიიღე_თარიღი():
    დღე = int(input("day: "))
    თვე = int(input("month: "))
    წელი = int(input("year: "))
    return f"{დღე}/{თვე}/{წელი}"

print(მიიღე_თარიღი())