from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    
    path('log',views.loged,name='loged'),
    path('manager',views.admin,name='admin'),
    path('registers',views.reg,name='reg'),
    path('view',views.view,name='view'),
    path('regedit/<int:id>',views.regedit,name='regedit'),
    path('regupdate/<int:id>',views.regupdate,name='regupdate'),
    path('teacher',views.teacher,name='teacher'),
    path('regdelete/<int:id>',views.regdelete,name='regdelete'),
    path('teacherview',views.teacherview,name='teacherview'),
    path('editteacher',views.editteacher,name='editteacher'),
    path('regstudent',views.regstudent,name='regstudent'),
    path('studentapproval',views.studentapproval,name='studentapproval'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.studentreject,name='studentreject'),
    path('studentview',views.studentview,name='studentview'),
    path('studentprofileview',views.studentprofileview,name='studentprofileview'),
    path('student',views.student,name='student'),
    path('teacherstudentview',views.teacherstudentview,name='teacherstudentview'),
    path('studentteacherview',views.studentteacherview,name='studentteacherview'),
    path('studentprofileview',views.studentprofileview,name='studentprofileview'),
    path('studentprofileedit',views.studentprofileedit,name='studentprofileedit'),
    path('studentprofileupdate/<int:id>',views.studentprofileupdate,name='studentprofileupdate'),
    path('applyleave', views.applyleave, name='applyleave'),
    path('leavestatus', views.leavestatus, name='leavestatus'),
    

    path('logouts',views.logouts,name='logouts'),




    

]