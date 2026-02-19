#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py - Интегрированный запускаемый файл для ЛР№4 и ЛР№5
============================================================

Использование:
    python main.py 1           # Part 1: Инкапсуляция (ЛР№4)
    python main.py 2           # Part 2: Наследование (ЛР№4)
    python main.py 3           # Part 3: Полиморфизм (ЛР№4)
    python main.py 4           # Part 4: Композиция (ЛР№4)
    python main.py all_lr4     # Все части ЛР№4
    python main.py patterns    # Все паттерны ЛР№5
    python main.py all         # Всё (ЛР№4 + ЛР№5)
    python main.py help        # Справка
"""

import sys
import os
from datetime import datetime

# Добавляем paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'examples'))


def print_header(title: str, separator: str = "=") -> None:
    """Печать красивого заголовка."""
    width = 80
    print(f"\n{separator * width}")
    print(f"  {title.center(width - 4)}")
    print(f"{separator * width}\n")


def print_help() -> None:
    """Показать справку."""
    print_header("СПРАВКА: ДОСТУПНЫЕ КОМАНДЫ", "=")
    
    help_text = """
  python main.py 1          Part 1: Инкапсуляция
                            - Класс Employee с приватными атрибутами
                            - Properties с валидацией
                            - Getter/Setter методы

  python main.py 2          Part 2: Наследование и абстракция
                            - AbstractEmployee интерфейс
                            - Manager, Developer, Salesperson
                            - EmployeeFactory

  python main.py 3          Part 3: Полиморфизм и магические методы
                            - Department с магическими методами
                            - __eq__, __lt__, __add__, __radd__
                            - Сериализация JSON

  python main.py 4          Part 4: Композиция и агрегация
                            - Project (композиция)
                            - Company (агрегация)
                            - Экспорт CSV

  python main.py all_lr4    Запустить ВСЕ части ЛР№4

  python main.py patterns   Все 13 паттернов проектирования
                            
                            Порождающие (4):
                            1. Singleton - БД
                            2. Factory Method - создание
                            3. Abstract Factory - семейства
                            4. Builder - пошаговое
                            
                            Структурные (3):
                            5. Adapter - интеграция
                            6. Decorator - расширение
                            7. Facade - упрощение
                            
                            Поведенческие (3):
                            8. Observer - уведомления
                            9. Strategy - алгоритмы
                            10. Command - история
                            
                            Доступ (3):
                            11. Repository - инкапсуляция
                            12. Specification - критерии
                            13. Unit of Work - транзакции


  python main.py all        Запустить ВСЁ (ЛР№4 + ЛР№5)

  python main.py help       Показать эту справку

  # Запустить Part 1
  $ python main.py 1

  # Запустить всю ЛР№4
  $ python main.py all_lr4

  # Запустить паттерны
  $ python main.py patterns

  # Запустить всё
  $ python main.py all

  # Справка
  $ python main.py help
"""
    print(help_text)
    print_header("КОНЕЦ СПРАВКИ", "=")


def run_part1() -> None:
    """Запустить Part 1: Инкапсуляция."""
    print_header("ЛР№4 - PART 1: ИНКАПСУЛЯЦИЯ", "═")
    
    try:
        from examples.test_part1 import TestPart1
        TestPart1.run()
        print("\n✅ Part 1 успешно завершена")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("   Убедитесь, что существует файл examples/test_part1.py")
    except Exception as e:
        print(f"❌ Ошибка при запуске Part 1: {e}")


def run_part2() -> None:
    """Запустить Part 2: Наследование."""
    print_header("ЛР№4 - PART 2: НАСЛЕДОВАНИЕ И АБСТРАКЦИЯ", "═")
    
    try:
        from examples.test_part2 import TestPart2
        TestPart2.run()
        print("\n✅ Part 2 успешно завершена")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("   Убедитесь, что существует файл examples/test_part2.py")
    except Exception as e:
        print(f"❌ Ошибка при запуске Part 2: {e}")


def run_part3() -> None:
    """Запустить Part 3: Полиморфизм."""
    print_header("ЛР№4 - PART 3: ПОЛИМОРФИЗМ И МАГИЧЕСКИЕ МЕТОДЫ", "═")
    
    try:
        from examples.test_part3 import TestPart3
        TestPart3.run()
        print("\n✅ Part 3 успешно завершена")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("   Убедитесь, что существует файл examples/test_part3.py")
    except Exception as e:
        print(f"❌ Ошибка при запуске Part 3: {e}")


def run_part4() -> None:
    """Запустить Part 4: Композиция."""
    print_header("ЛР№4 - PART 4: КОМПОЗИЦИЯ И АГРЕГАЦИЯ", "═")
    
    try:
        from examples.test_part4 import TestPart4
        TestPart4.run()
        print("\n✅ Part 4 успешно завершена")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("   Убедитесь, что существует файл examples/test_part4.py")
    except Exception as e:
        print(f"❌ Ошибка при запуске Part 4: {e}")


def run_patterns() -> None:
    """Запустить демонстрацию паттернов ЛР№5."""
    print_header("ЛР№5: ДЕМОНСТРАЦИЯ ПАТТЕРНОВ ПРОЕКТИРОВАНИЯ", "═")
    
    try:
        from examples.test_patterns import PatternDemonstration
        PatternDemonstration.demonstrate_all_patterns()
        print("\n✅ Все паттерны успешно демонстрированы")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("   Убедитесь, что существует файл examples/test_patterns.py")
    except AttributeError as e:
        print(f"❌ Ошибка атрибута: {e}")
        print("   Класс PatternDemonstration не имеет метода demonstrate_all_patterns()")
    except Exception as e:
        print(f"❌ Ошибка при запуске паттернов: {e}")
        import traceback
        traceback.print_exc()


def run_all_lr4() -> None:
    """Запустить все части ЛР№4."""
    print_header("ЛР№4: ВСЕ ЧАСТИ (1-4)", "▓")
    
    run_part1()
    run_part2()
    run_part3()
    run_part4()
    
    print_header("ЛР№4: ВСЕ ЧАСТИ ЗАВЕРШЕНЫ", "▓")


def run_all() -> None:
    """Запустить ВСЁ (ЛР№4 + ЛР№5)."""
    print_header("ПОЛНЫЙ ЗАПУСК: ЛР№4 + ЛР№5", "█")
    
    # ЛР№4
    run_all_lr4()
    
    # ЛР№5
    print("\n")
    run_patterns()
    
    # Итоги
    print_header("ПОЛНЫЙ ЗАПУСК ЗАВЕРШЁН", "█")
    print(f"✅ Время завершения: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


def main() -> None:
    """Главная функция."""
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'help':
        print_help()
    elif command == '1':
        run_part1()
    elif command == '2':
        run_part2()
    elif command == '3':
        run_part3()
    elif command == '4':
        run_part4()
    elif command == 'all_lr4':
        run_all_lr4()
    elif command == 'patterns':
        run_patterns()
    elif command == 'all':
        run_all()
    else:
        print(f"❌ Неизвестная команда: {command}")
        print("   Используйте 'python main.py help' для справки")
        sys.exit(1)


if __name__ == '__main__':
    main()
