# # task 1
def is_admin(func):
    def inner(**params):
        user_type = params['user_type']
        if user_type != 'admin':
            raise ValueError("Permission denied")
        
        return func(user_type)
    return inner

@is_admin
def show_customer_receipt(user_type: str):
    print("function pass as it should be")

show_customer_receipt(user_type='admin')
print('-----------')
show_customer_receipt(user_type='user')

# task 2

def catch_errors(func):
    def wrapper(params):
        try:
            func(params)
        except KeyError as error:
            print('Occured KeyError: no such key as ' + str(error))
            
        except Exception as error:
            template = "An exception of type {0} occurred with message: {1}"
            message = template.format(type(error).__name__, str(error))
            print(message)
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})
print('------------------------------------')
some_function_with_risky_operation({'key': 'bar'})