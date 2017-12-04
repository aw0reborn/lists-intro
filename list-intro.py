### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def calculate_sgpa(c):
    if type(c)!= list:
        c = [c]
    if not c:
        return 0
    total_marks=0
    total_subjects=0
    if c == None:
        return None
    x = len(c)
    total_subjects += x
    if x == 0:
        return None
    for i in c:
        if i == 'None':
            return None
  
        if i == 'A+':
            total_marks += 4.0
            continue
        if i == 'A':
            total_marks += 4.0
            continue
        if i == 'A-':
            total_marks += 3.67
            continue
        if i == 'B+':
            total_marks += 3.33
            continue
        if i == 'B':
            total_marks += 3.0
            continue
        if i == 'B-':
            total_marks += 2.67
            continue
        if i == 'C+':
            total_marks += 2.33
            continue
        if i == 'C':
            total_marks += 2.0
            continue
        if i == 'C-':
            total_marks += 1.67
            continue
        if i == 'D+':
            total_marks += 1.33
            continue
        if i == 'D':
            total_marks += 1.0
            continue
        if i == 'F':
            total_marks += 0
            continue
        else:
            return None
    sgpa = total_marks/total_subjects
    return sgpa
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(c,d):
    list()
    if type(c) != list:
        c = [c]
    if type(d) != list:    
        d = [d]
    
    if len(c) != len(d):
        return None
    if len(c)==0 or len(d)==0:
        return None
    total_marks = []
    list1 = []
    w = sum(d)
    if c == None:
        return None

    for i in c:
        if i == 'None':
            return None
  
        if i == 'A+':
            total_marks.append(4.0)
            continue
        if i == 'A':
            total_marks.append(4.0)
            continue
        if i == 'A-':
            total_marks.append(3.67)
            continue
        if i == 'B+':
            total_marks.append(3.33)
            continue
        if i == 'B':
            total_marks.append(3.0)
            continue
        if i == 'B-':
            total_marks.append(2.67)
            continue
        if i == 'C+':
            total_marks.append(2.33)
            continue
        if i == 'C':
            total_marks.append(2.0)
            continue
        if i == 'C-':
            total_marks.append(1.67)
            continue
        if i == 'D+':
            total_marks.append(1.33)
            continue
        if i == 'D':
            total_marks.append(1.0)
            continue
        if i == 'F':
            total_marks.append(0)
            continue
        else:
            return None
    for i in total_marks:
        for y in d:
            a = i*y
            list1.append(a)
            d.remove(y)
            break
    q = sum(list1)
    SGPA = q/w
    return SGPA

#### End OF MARKER

