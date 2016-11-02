def remove_duplicates(Lst):
    Lr = []
    for i in Lst:
        if i not in Lr:
            Lr.append(i)
    return Lr
