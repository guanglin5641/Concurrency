from django.shortcuts import render
import time
import pymysql
import requests
import json
from collections import defaultdict
# views.py
from django.shortcuts import render
from .utils import fangfa

def shop_analysis_view(request):
    shops_with_district, shops_without_district = fangfa()
    context = {
        'shops_with_district': shops_with_district,
        'shops_without_district': shops_without_district,
    }
    return render(request, 'shop_analysis.html', context)
