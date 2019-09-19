students = ["ivanov", "sidorov", "petrov", "cortosha"]
marks = [[12, 6, 8, 11], [5, 6, 7, 8],
[12, 12, 12, 11],[4, 9, 8, 6]]
jornal = dict(zip(students, marks))
print(jornal)

def sred_marks(mark):
    sredbal = {}
    for surname, mark_list in mark.items():
        sredzn = sum(mark_list)/len(mark_list)
        sredbal[surname] = sredzn
    # словарь {"ivanov" : 9.25, ....}

    tuple1 = sredbal.popitem()
    # tuple("ivanov",9.25)
    max_bal =  min_bal = tuple1[1]
    # float(9.25)
    max_bal_surname = min_bal_surname = tuple1[0]
    # str("ivanov")

    for surname, sredzn in sredbal.items():
        if(sredzn > max_bal):
            max_bal = sredzn
            max_bal_surname = surname
        if(sredzn < min_bal):
            min_bal = sredzn
            min_bal_surname = surname

    return {
        "maximum": (max_bal_surname, max_bal),
        "minimum": (min_bal_surname, min_bal)
    }   
print (sred_marks(jornal))
