from rest_framework.response import Response
from rest_framework.views import APIView
from publication.serializers import PublicationSerializer, PublicationInputSerializer, LikeSerializer
from publication.services import PublicationService



class PublicationView(APIView):

    @staticmethod
    def get(request):
        user = request.user
        publications = PublicationService.get_all_publications()
        for publication in publications:
            publication.number_likes = PublicationService.get_likes(publication)
            publication.has_user_liked = PublicationService.has_user_liked(publication, user)

        response = PublicationSerializer(publications, many=True)
        return Response(response.data, status=200)

    @staticmethod
    def post(request):
        user = request.user
        publication_input = PublicationInputSerializer(data =request.data)
        if not publication_input.is_valid():
            return Response({"message": "Invalid input. Expected 'title' and 'body'"}, status=400)

        try:
            publication = PublicationService.create_publication(user, publication_input.validated_data)
            response = PublicationInputSerializer(publication)
            return Response(response.data, status=201)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    @staticmethod
    def put(request, publication_id):
        user = request.user

        publication_input = PublicationInputSerializer(data=request.data)
        if not publication_input.is_valid():
            return Response({"message": "Invalid input. Expected 'title' and 'body'"}, status=400)

        try :
            edited_publication = PublicationService.edit_my_publication(user, publication_id, publication_input.validated_data)
            response = PublicationInputSerializer(edited_publication)
            return Response(response.data, status=200)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    @staticmethod
    def delete(request, publication_id):
        PublicationService.delete_my_publication(request.user, publication_id)
        return Response({"message": "Publication deleted successfully"}, status=200)

########################################################################################################################
class LikeView(APIView):
    @staticmethod
    def post(request, publication_id):
        try:
            like = PublicationService.like_publication(publication_id, request.user)
            response = LikeSerializer(like)
            return Response(response.data, status=201)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    @staticmethod
    def delete(request, publication_id):
        try:
            like = PublicationService.dislike_publication(publication_id, request.user)
            response = LikeSerializer(like)
            return Response(response.data, status=200)
        except Exception as e:
            return Response({"message": str(e)}, status=400)