def mark_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '/<b>'
    return wrapper

def mark_italic(func):
    def wrapper(*args, **kwargs):
        return '<i>' + func(*args, **kwargs) + '/<i>'
    return wrapper


@mark_bold
@mark_italic
def add_html(string):
    return string

print(add_html('안녕'))
