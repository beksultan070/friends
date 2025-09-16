from .models import  SocialNetwork, Category, Project, Offer
from modeltranslation.translator import TranslationOptions,register



@register(SocialNetwork)
class SocialNetworkTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)



@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ('message',)




