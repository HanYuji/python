def print_hello(name):
    print("Hello", name)

print_hello('miso1')

print_hello_name = print_hello
print_hello_name('miso2')

func_list = [print_hello, 1, 2]
func_list[0]('miso3')

func_dict = {
    'func' : print_hello
}
func_dict['func']('miso4')