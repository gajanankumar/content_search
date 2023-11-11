from django.shortcuts import render

# Create your views here.
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import F
from django.shortcuts import render
from .models import Article, Image, Video

def search(request):
    query = request.GET.get('q', '')
    if query:
        # Perform search using search vector and rank results
        article_results = Article.objects.annotate(rank=SearchRank(F('search_vector'), SearchQuery(query))).order_by('-rank')
        image_results = Image.objects.annotate(rank=SearchRank(F('search_vector'), SearchQuery(query))).order_by('-rank')
        video_results = Video.objects.annotate(rank=SearchRank(F('search_vector'), SearchQuery(query))).order_by('-rank')
    else:
        article_results = image_results = video_results = []

    return render(request, 'search_results.html', {
        'query': query,
        'article_results': article_results,
        'image_results': image_results,
        'video_results': video_results,
    })
