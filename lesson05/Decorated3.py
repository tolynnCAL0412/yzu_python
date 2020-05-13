def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def make_shoes(func):
    def dress():
        print("穿鞋子")
        func()
    return dress

@make_dress
@make_shoes
def out():
    print("我出門了")

out()
