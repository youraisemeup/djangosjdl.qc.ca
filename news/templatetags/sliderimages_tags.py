from django.template import Library, Node, Variable, VariableDoesNotExist
register = Library()

class GetGalleryImages(Node):
    def __init__(self,ik_diapo, varname):
        self.ik_diapo, self.varname = Variable(ik_diapo), varname

    def render(self,context):
        from mezzanine.galleries.models import Gallery
        from mezzanine.galleries.models import GalleryImage
        #print(self.ik_diapo.resolve(context))
        try:
            actual_ik_diapo = self.ik_diapo.resolve(context)
            gallery = Gallery.objects.get(id=actual_ik_diapo)
            images = GalleryImage.objects.all().filter(gallery_id=gallery.id)
            context[self.varname] = images
            return ''
        except VariableDoesNotExist:
            return ''

def get_gallery_images(parser, token):
    bits = token.contents.split()
    if len(bits) !=4:
        raise TemplateSyntaxError, "get_gallery_images takes 1 argument only"
    return GetGalleryImages(bits[1], bits[3])

get_gallery_images = register.tag(get_gallery_images)