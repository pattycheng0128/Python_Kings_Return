#傳回多筆資料的應用
def englishname(firstname, lastname):
    name = lastname.title() + firstname.title()
    print(name)
    return name

name = englishname("cheng","patty")