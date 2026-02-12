def meu_decorator(func):
    def wrapper(*args, **kwargs):
        # comportamento extra ANTES
        resultado = func(*args, **kwargs)
        # comportamento extra DEPOIS
        return resultado
    return wrapper


