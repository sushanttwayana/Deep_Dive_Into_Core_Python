def is_an_adult(age:int, has_id:bool) -> bool:
    return age >= 21 and has_id

def is_bob(name: str) -> bool:
    return name.lower() == 'bob'

def enter_club(name:str, age:int, has_id:bool) -> None:

    if is_bob(name):
        print(f'Get out of here {name}, we want no trouble')
        return
    
    if is_an_adult(age, has_id):
        print(f'{name}, you may enter the club')

    else:
        print(f"{name}, you are not allowed to enter the club")

def main() -> None:
    enter_club('Bob', 29, has_id=True)
    enter_club('Alexa', 25, has_id=True)
    enter_club('Mark', 19, has_id=True)
    enter_club('Troy', 22, has_id=False)


if __name__ == '__main__':

    main()