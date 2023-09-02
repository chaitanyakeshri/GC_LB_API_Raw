from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, GCsSerializer, HostelSerializer, GCsNameSerializer, Score_BoardSerializer
from articles.models import Article , GCs , Score_Board , Hostel
#from django.db.models import F
#from collections import defaultdic





@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create' : 'api/add',
        'Read' : 'api/get',
        'Update' : 'api/update',
        'Delete' : 'api/delete'

    }

    return Response(api_urls)


@api_view(['GET'])  # this is callled a decorator
def getData(request):
   
    article = Article.objects.all()
    serializer  = ArticleSerializer(article, many = True )
    return Response(serializer.data)


@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateArticle(request,pk):
    article = Article.objects.get(id = pk)
    serializer = ArticleSerializer(instance= article ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteArticle(request,pk):
    article = Article.objects.get(id = pk)
    article.delete()
    return Response("Article sucessfuly deleted")

#####################################################################################
""" 1 """
@api_view(['GET'])  # display static data cult tech sports
def Types_Of_GCs(request):
   
   types = [ "Cult" , "Tech" , "Sports"]
   return Response(types)

#####################################################################################
""" 2 """
@api_view(['GET'])  # to get list of all the cult GCs
def Cult_GC(request):
   
    gc = GCs.objects.filter(GC_Type = 'Cult').values_list('GC_Name', flat=True)
    #serializer  = GCsNameSerializer(gc, many = True )
    return Response(gc)


@api_view(['GET'])  # to get list of all tech gcs
def Tech_GC(request):
   
    gc = GCs.objects.filter(GC_Type = 'Tech').values_list('GC_Name', flat=True)
     #serializer  = GCsNameSerializer(gc, many = True )
    return Response(gc)

@api_view(['GET'])  # to get list of all sports gc
def Sports_GC(request):
   
    gc = GCs.objects.filter(GC_Type = 'Sports').values_list('GC_Name', flat=True)
    #serializer  = GCsNameSerializer(gc, many = True )
    return Response(gc)

#######################################################################################

""" 3 """
@api_view(['GET'])  # to get list of all sports gc
def Sub_GC_LB(request, gc_ID):
   
    gc = Score_Board.objects.filter(GC_ID = gc_ID).values_list('Points_Array', flat=True)
    #serializer  = GCsNameSerializer(gc, many = True )
    Dict_GC = gc[0]
    sorted_dict = dict(sorted(Dict_GC.items(), key=lambda item: item[1], reverse= True))
    return Response(sorted_dict)

""" 4
@api_view(['GET'])  # to get list of all sports gc
def Type_GC_LB(request, type):
    if type in ['Cult_Points', 'Tech_Points', 'Sports_Points']:
        sorted_hostels = Hostel.objects.all().order_by(F(type).desc())
        serializer = HostelSerializer(sorted_hostels, many=True)
        return Response(serializer.data)
"""   

""" 4 """
@api_view(['GET'])  # to get list of all sports gc
def Type_GC_LB(request, type):
    sorted_hostels = Hostel.objects.values('name', type).order_by('-'+ type)
    #serializer = HostelSerializer(sorted_hostels, many=True)
    return Response(sorted_hostels)

""" 5 """
@api_view(['GET'])  # to get list of all sports gc
def GC_LB(request):
    sorted_hostels = Hostel.objects.values('name','Total_Points' ).order_by('-Total_Points')
    #serializer = HostelSerializer(sorted_hostels, many=True)
    return Response(sorted_hostels)


""" 6 """

@api_view(['POST'])
def add_GC(request):
    serializer = GCsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

""" 7 """
@api_view(['PUT'])
def update_Points(request):
    serializer = Score_BoardSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    #reflector(serializer.data)
    
    return Response(serializer.data)
'''
def reflector(data):
    raw_data = data[0]
    
    

    if(GCs.raw_data[GC_ID]    ) 

'''