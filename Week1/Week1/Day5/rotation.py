def find_rotation_point(alphabets):
    for i in range(len(alphabets)-1):
        if alphabets[i]>alphabets[i+1]:
            return i+1


