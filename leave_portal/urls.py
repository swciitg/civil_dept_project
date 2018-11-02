from django.urls import path,include
from . import views

app_name = "leave_portal"
urlpatterns = [
    path('',views.index , name="HelloWorld"),


    path('dashboard', views.dashboard , name='dashboard'),
    path('dppc/updatedppcdata/<int:pk>',views.DppcUpdateDetail, name="dppc_detail_update"),
    path('dppc/updatehoddata/<int:pk>',views.HodUpdateDetail, name="hod_detail_update"),
    path('dppc/updatestaffdata/<int:pk>',views.StaffUpdateDetail, name="staff_detail_update"),



    path('student',views.StudentListView.as_view() , name="studentsList" ),
    path('students/updatedata/<int:pk>',views.StudentUpdateDetail, name="stud_detail_update"),
    path('student/<int:pk>',views.StudentDetailView.as_view(), name="studentsDetail" ),
    path('student/leaveform/<int:pk>', views.ApplyLeave, name="apply_leave"),
    path('student/leaveform/<int:pk>/<int:leave_id>', views.ApplyLeaveEdit, name="apply_leave_edit"),
    path('student/<int:pk>/pending', views.PendingRequest,name="pending_request"),
    path('dppc/pending_request',views.dppc_pending,name="dppc_pending_request"),
    path('dppc/pending_request/approve/<int:pk>',views.approveleave,name="Approve"),
    path('dppc/pending_request/decline/<int:pk>',views.declineleave,name="Decline"),
    path('dppc',views.DppcListView.as_view(), name="dppclist"),
    path('dppc/<int:pk>',views.DppcDetailView.as_view(), name="dppcdetail"),



]
