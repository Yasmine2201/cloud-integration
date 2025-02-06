from django.utils import timezone

from publication.models import Publication, Comment, Like


class PublicationService:

    @staticmethod
    def create_publication(title, body, publisher):
        publication = Publication(title=title, body=body, publisher=publisher)
        publication.save()
        return publication

    @staticmethod
    def get_my_publication(publisher):
        return Publication.objects.get(publisher=publisher)

    @staticmethod
    def edit_my_publication(publisher, title, body):
        publication = Publication.objects.get(publisher=publisher)
        publication.title = title
        publication.body = body
        publication.save()
        return publication

    @staticmethod
    def delete_my_publication(publisher):
        publication = Publication.objects.get(publisher=publisher)
        publication.delete()
        return publication

    @staticmethod
    def publish_my_publication(publisher):
        publication = Publication.objects.get(publisher=publisher)
        publication.published_at = timezone.now()
        publication.save()
        return publication

    @staticmethod
    def get_last_publication():
        return Publication.objects.filter(published_at__isnull=False).last()
##################################################################
    @staticmethod
    def comment_publication(publication, author, body):
        comment = Comment(publication=publication, author=author, body=body)
        comment.save()
        return comment

    @staticmethod
    def get_comments(publication):
        return Comment.objects.filter(publication=publication)
#######################################################################
    @staticmethod
    def like_publication(publication, author):
        like = Like(publication=publication, author=author, is_liked=True)
        like.save()
        return like

    @staticmethod
    def dislike_publication(publication, author):
        like = Like(publication=publication, author=author, is_liked=False)
        like.save()
        return like

    @staticmethod
    def get_likes(publication):
        return Like.objects.filter(publication=publication)
