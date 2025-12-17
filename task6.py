class NameLengthError(ValueError):
    def __init__(self, name):
        message = f"Виняток: Довжина імені '{name}' менша 10 символів!"
        super().__init__(message)

def check_name_length(name):
    if len(name) < 10:
        raise NameLengthError(name)
    else:
        pass


names = ["Oleksandr", "Oleksandr_Nechai", "Nechai"]

for n in names:
    try:
        check_name_length(n)
        print(f"Ім'я '{n}' перевірку пройшло.")
    except NameLengthError as e:
        print(e)