from django.urls import path, re_path
from apps.home import  views
from . import axios

urlpatterns = [
    
    # post
    path('Inpsetting/',axios.Inpsetting),
    path('connect_server/',axios.connect_server),
    path('SaveRevise/',axios.SaveRevise),
    path('item_check/',axios.item_check),
    path('table1_0/',axios.table1_0),
    path('SaveHistory/',axios.SaveHistory),
    path('getHistory/',axios.getHistory),
    path('SaveTable/',axios.SaveTable),
    path('recover/',axios.recover),
    
    
    
    # get 
    path('GetDashboard/',axios.GetDashboard),
    path('GetLngLat/',axios.GetLngLat),
    path('GetTable/',axios.GetTable),
    path('GetExport/',axios.GetExport),
    path('GetDownload/',axios.GetDownload),
    

    # show
    path('DashBoard.html',axios.showDashboard),
    path('history.html',axios.showHistory),
    path('settings.html',axios.showSetting),
    path('page-revise.html',axios.showRevise),
    

    

    # The home page
    path('', axios.showDashboard, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages')
    
    
    
    

]
