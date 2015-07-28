from . import tasks
from apex import celery_app
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.reverse import reverse


class SumViewSet(ViewSet):
    def create(self, request, format=None):
        # XXX Do some validation, maybe with jsonschema
        elements = request.data

        task = tasks.AddTheThings()
        task_result = task.delay(elements)

        return Response(data={}, status=202, headers={
            'Location': reverse('sum-detail', args=[str(task_result.task_id)],
                                request=request),
        })

    def retrieve(self, request, pk=None):
        task_result = celery_app.app.AsyncResult(pk)
        if task_result.ready():
            total = task_result.get()
            return Response(status=200, data={
                'status': 'SUCCESS',
                'total': total,
            })

        else:
            return Response(status=206, data={
                'status': 'PENDING',
            })
