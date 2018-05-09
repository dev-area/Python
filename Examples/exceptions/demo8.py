class CustomException(Exception):
    def __str__(self):
        return "custom error"
    pass

def fn(*arguments):
    if not all(arguments):
        raise CustomException("False argument in fn")


try:
    fn('dev','',42)
except CustomException as err:
    print("Oops:" ,err )
