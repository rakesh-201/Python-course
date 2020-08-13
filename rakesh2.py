class Hello:
    def __init__(a, name, id):
        a.name=name;
        a.id=id
    @classmethod
    def str_space(c, st):
        rak=st.split(" ")
        print(rak)
        return c(*rak)
    
rocky = Hello.str_space("rocky 19191919")
ra=["r",1919]
print(rocky)
print(Hello("r",1919))
print(Hello("ra",1919))