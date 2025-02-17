from publication.models import Publication, Like


class PublicationService:

    @staticmethod
    def create_publication(title, body, publisher):
        publication = Publication(title=title, body=body, publisher=publisher)
        publication.save()
        return publication

    @staticmethod
    def get_publication_by_id(user, publication_id):
        publication = Publication.objects.get(id=publication_id)
        if publication.publisher == user:
            return publication
        return Exception("You are not the publisher of this publication")

    @staticmethod
    def edit_my_publication(user, publication_id, title, body):
        publication = PublicationService.get_publication_by_id(user, publication_id)

        publication.title = title
        publication.body = body
        publication.save()
        return publication

    @staticmethod
    def delete_my_publication(user, publication_id):
        publication = PublicationService.get_publication_by_id(user, publication_id)
        publication.delete()
        return publication

    @staticmethod
    def get_all_publications(user=None):
        if user is None:
            return Publication.objects.all().order_by('-created_at')

        return Publication.objects.exclude(publisher=user).all().order_by('-created_at')

    ##################################################################
    @staticmethod
    def like_publication(publication, author):

        if not Like.objects.filter(publication=publication, author=author).exists():
            like = Like(publication=publication, author=author, is_liked=True)
            like.save()
            return like

        else:
            like = Like.objects.get(publication=publication, author=author)
            like.is_liked = True
            like.save()
            return like

    @staticmethod
    def dislike_publication(publication, author):
        if not Like.objects.filter(publication=publication, author=author).exists():
            dislike = Like(publication=publication, author=author, is_liked=False)
            dislike.save()
            return dislike
        else:
            dislike = Like.objects.get(publication=publication, author=author)
            dislike.is_liked = False
            dislike.save()

        return dislike

    @staticmethod
    def get_likes(publication):
        return Like.objects.filter(publication=publication, is_liked=True).count()

    @staticmethod
    def get_dislikes(publication):
        return Like.objects.filter(publication=publication, is_liked=False).count()

    @staticmethod
    def has_user_liked(publication, user):
        return Like.objects.filter(publication=publication, author=user, is_liked=True).exists()
