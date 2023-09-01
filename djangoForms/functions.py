from turtledemo.penrose import f


def handle_uploaded_files():
    with open('djangoForms/static/upload' + f.name, 'wb+') as destinaton:
        for chumk in f.chunks():
            destinaton.write(chumk)
