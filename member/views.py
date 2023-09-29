from rest_framework import decorators, serializers
from drf_spectacular.utils import extend_schema, inline_serializer
from drf_spectacular.types import OpenApiTypes
import json
from django.http import JsonResponse


@extend_schema(
    request=inline_serializer(
        name="MemberSerializer",
        fields={
            "loan_ids": serializers.ListField(),
        },
    ),
    responses=OpenApiTypes.OBJECT,
    methods=['POST'],
)
@decorators.api_view(http_method_names=['post'])
def post_member(request):
    request_body = json.loads(request.body.decode('utf-8'))
    return JsonResponse({'success': True, 'request': request_body}, status=200)
