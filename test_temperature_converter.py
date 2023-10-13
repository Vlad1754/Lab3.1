# test_temperature_converter.py

import temperature_converter

# Тести для перетворення температур з градусів Цельсія в градуси Фаренгейта
def test_celsius_to_fahrenheit():
    # Перевіряємо, чи правильно перетворюється 0 °C в 32 °F
    assert temperature_converter.celsius_to_fahrenheit(0) == 32.0
    # Перевіряємо, чи правильно перетворюється 100 °C в 212 °F
    assert temperature_converter.celsius_to_fahrenheit(100) == 212.0

# Тести для перетворення температур з градусів Фаренгейта в градуси Цельсія
def test_fahrenheit_to_celsius():
    # Перевіряємо, чи правильно перетворюється 32 °F в 0 °C
    assert temperature_converter.fahrenheit_to_celsius(32.0) == 0
    # Перевіряємо, чи правильно перетворюється 212 °F в 100 °C
    assert temperature_converter.fahrenheit_to_celsius(212.0) == 100
