from .models import Item, Box

def count_items(request):
    return {'count_items' : Item.objects.count()}

def packed_items(request):

    #packed_items = Item.objects.filter(boxed=True).count()

    items = Item.objects.all()
    count = 0
    for i in items:
        if i.boxed != None:
            count += 1

    packed_items = count


    return {'packed_items' : packed_items}