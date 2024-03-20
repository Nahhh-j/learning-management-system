from django.urls import path
from .views import CourseListCreate, CourseDetail, LectureListCreate, LectureDetail, ExamListCreate, ExamDetail, GradeListCreate, GradeDetail, CommunicationSend, ReceivedMessageList, SentMessageList, MessageDetail

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('lectures/', LectureListCreate.as_view(), name='lecture-list-create'),
    path('lectures/<int:pk>/', LectureDetail.as_view(), name='lecture-detail'),
    path('exams/', ExamListCreate.as_view(), name='exam-list-create'),
    path('exams/<int:pk>/', ExamDetail.as_view(), name='exam-detail'),
    path('grades/', GradeListCreate.as_view(), name='grade-list-create'),
    path('grades/<int:pk>/', GradeDetail.as_view(), name='grade-detail'),
    path('send-message/', CommunicationSend.as_view(), name='send-message'),
    path('received-messages/', ReceivedMessageList.as_view(), name='received-messages'),
    path('sent-messages/', SentMessageList.as_view(), name='sent-messages'),
    path('messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
]

