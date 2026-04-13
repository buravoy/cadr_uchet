import database
import analytics
import seed


def main():
    database.init_db()

    while True:
        print("\n=== Кадровый учёт ===")
        print("1. Показать всех сотрудников")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Средний оклад по отделам")
        print("5. Сгенерировать 10 тестовых записей")
        print("6. Удалить все тестовые данные")
        print("0. Выход")

        choice = input("Выберите: ")

        if choice == "1":
            rows = database.get_all_employees()
            for r in rows:
                print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")

        elif choice == "2":
            emp_id = int(input("Табельный номер: "))
            full_name = input("ФИО: ")
            department = input("Отдел: ")
            position = input("Должность: ")
            salary = float(input("Оклад: "))
            database.save_employee(emp_id, full_name, department, position, salary)
            print("Сотрудник сохранён.")

        elif choice == "3":
            emp_id = int(input("Табельный номер: "))
            database.delete_employee(emp_id)
            print("Сотрудник удалён.")

        elif choice == "4":
            rows = analytics.average_salary_by_department()
            for r in rows:
                print(f"{r[0]}: {r[1]:.2f}")

        elif choice == "5":
            employees = seed.generate_test_employees(10)
            database.add_test_employees(employees)
            print("10 тестовых записей добавлено.")

        elif choice == "6":
            database.delete_test_employees()
            print("Тестовые данные удалены.")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()