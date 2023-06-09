import pandas as pd
from django.http import HttpResponse

from rest_framework import mixins, generics, status
from rest_framework.response import Response

from .serializers import DeviceSerializer


class DeviceView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = DeviceSerializer.Meta.model.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = "pk"

    # Create Section
    def create(self, request, *args, **kwargs):
        """Create Device"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # data = serializer.validated_data   # Get Validated Data
        # df = pd.DataFrame([data])  # Create DataFrame
        # csv_data = df.to_csv(index=False)  # Create CSV String
        # response = HttpResponse(csv_data, content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="device.csv"'
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # List and Retrieve Section
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)  # for single device
        return self.list(request, *args, **kwargs)  # for all device

    # Update Section
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # Destroy Section

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        return super().destroy(instance)
