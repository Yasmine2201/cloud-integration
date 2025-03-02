from werkzeug.exceptions import Forbidden

from publication.models import Publication, Like


class PublicationService:

    @staticmethod
    def create_publication(publisher, publication_input):
        publication = Publication(title=publication_input.get("title"), body=publication_input.get("body"), publisher=publisher)
        publication.save()
        return publication

    @staticmethod
    def __get_publication_by_id(user, publication_id):
        publication = Publication.objects.get(id=publication_id)
        if publication.publisher == user:
            return publication
        else :
            raise Exception("You are not the publisher of this publication")

    @staticmethod
    def edit_my_publication(user, publication_id, publication_input):
        publication = PublicationService.__get_publication_by_id(user, publication_id)

        publication.title = publication_input.get("title")
        publication.body = publication_input.get("body")
        publication.save()
        return publication

    @staticmethod
    def delete_my_publication(user, publication_id):
        publication = PublicationService.__get_publication_by_id(user, publication_id)
        publication.delete()
        return publication

    @staticmethod
    def get_all_publications():
       return Publication.objects.all().order_by('-created_at')


    @staticmethod
    def get_my_publications(user):
        return Publication.objects.filter(publisher=user).all().order_by('-created_at')

    ##################################################################
    @staticmethod
    def like_publication(publication_id, author):
        publication_instance = Publication.objects.get(id=publication_id)
        if not Like.objects.filter(publication=publication_instance, author=author).exists():
            like = Like(publication=publication_instance, author=author)
            like.save()
            return like
        else:
            raise Exception("You have already liked this publication")

    @staticmethod
    def dislike_publication(publication_id, author):
        publication_instance = Publication.objects.get(id=publication_id)
        if not Like.objects.filter(publication=publication_instance, author=author).exists():
            raise Exception("You have not liked this publication")

        like = Like.objects.get(publication=publication_instance, author=author)
        like.delete()
        return like

    @staticmethod
    def get_likes(publication):
        return Like.objects.filter(publication=publication).count()

    @staticmethod
    def has_user_liked(publication, user):
        return Like.objects.filter(publication=publication, author=user).exists()
