# coding: utf-8
def iscontained_step1(contained, container):
    return True


iscontained = iscontained_step1


def iscontained_step2(contained, container):
    return contained == container


iscontained = iscontained_step2


def iscontained_step3(contained, container):
    return contained == []


iscontained = iscontained_step3


def iscontained_step4(contained, container):
    if contained == [] or contained == container:
        return True
    else:
        return False


iscontained = iscontained_step4


def iscontained_step5(contained, container):
    if contained == []:
        return True
    else:
        return contained[0] in container


iscontained = iscontained_step5


def iscontained_step6(contained, container):
    for item in contained:
        if item not in container:
            return False
    return True


iscontained = iscontained_step6
