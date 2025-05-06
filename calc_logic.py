# Função Calculadora

def insert_value(value, text_var):
    current = text_var.get()
    text_var.set(current + value)
def clear(text_var):
    text_var.set("")
def calculate(text_var):
    try:
        question = text_var.get().replace('x', '*').replace('÷', '/')
        result = str(eval(question))
        text_var.set(result)
    except Exception:
        text_var.set('Erro.')