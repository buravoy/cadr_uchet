import random

NAMES = [
    "Иванов И.И.", "Петров П.П.", "Сидоров С.С.", "Козлов К.К.",
    "Новиков Н.Н.", "Морозов М.М.", "Волков В.В.", "Соколов С.С.",
    "Лебедев Л.Л.", "Кузнецов К.К.", "Попов П.П.", "Орлов О.О."
]

DEPARTMENTS = ["Бухгалтерия", "ИТ", "Отдел кадров", "Маркетинг", "Логистика"]

POSITIONS = [
    "Специалист", "Ведущий специалист", "Начальник отдела",
    "Программист", "Аналитик", "Менеджер"
]


def generate_test_employees(count=10):
    employees = []
    for i in range(count):
        emp_id = random.randint(9000, 9999)
        full_name = random.choice(NAMES)
        department = random.choice(DEPARTMENTS)
        position = random.choice(POSITIONS)
        salary = random.randint(30000, 120000)
        employees.append((emp_id, full_name, department, position, salary))
    return employees