def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    temperatura_f = celsius_para_fahrenheit(25)
    print(f"25°C em Fahrenheit: {temperatura_f}°F")
