from django.utils.text import slugify

def gerador_slug_unica(instancia_model, titulo, campo_slug):
    slug = slugify(titulo)
    model_class = instancia_model.__class__
    while model_class._default_manager.filter(slug=slug).exists():
        obj_id = model_class._default_manager.latest('id')
        obj_id = obj_id.id + 1
        slug = f'{slug}-{obj_id}'

    return slug