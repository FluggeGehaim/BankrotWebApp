from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

from goods.models import Lots


def q_search(query):
    if query.isdigit() and len(query) <= 6:
        return Lots.objects.filter(id=int(query))
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    return Lots.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_object = Q()
    #
    # for token in keywords:
    #     q_object |= Q(description__icontains=token)
    #     q_object |= Q(name__icontains=token)
    #
    # return Lots.objects.filter(q_object)
