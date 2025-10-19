# age :int
# number:str
# is_human:bool
# height:float

def age_check(age:int) -> bool:
    if age > 18:
        can_drive = True

    else:
        can_drive = False

    return can_drive

print(age_check(12))    