from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404  # Http404 추가
from .models import Course, Lecture, Exam, Grade, Communication
from .serializers import CourseSerializer, LectureSerializer, ExamSerializer, GradeSerializer, CommunicationSerializer

class CourseListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request):
        courses = Course.objects.filter(teacher=request.user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk, teacher=self.request.user)  # request 수정
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class LectureListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request):
        lectures = Lecture.objects.filter(course__teacher=request.user)
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LectureDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self, pk):
        try:
            return Lecture.objects.get(pk=pk, course__teacher=self.request.user)
        except Lecture.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)

    def put(self, request, pk):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(lecture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lecture = self.get_object(pk)
        lecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ExamListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()
    
    def get(self, request):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExamDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()
    
    def get_object(self, pk):
        try:
            return Exam.objects.get(pk=pk)
        except Exam.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        exam = self.get_object(pk)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

    def put(self, request, pk):
        exam = self.get_object(pk)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        exam = self.get_object(pk)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GradeListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()
    
    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GradeDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()
    
    def get_object(self, pk):
        try:
            return Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        grade = self.get_object(pk)
        serializer = GradeSerializer(grade)
        return Response(serializer.data)

    def put(self, request, pk):
        grade = self.get_object(pk)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        grade = self.get_object(pk)
        grade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommunicationSend(APIView):
    def post(self, request):
        serializer = CommunicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceivedMessageList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        received_messages = Communication.objects.filter(receiver_id=request.user.id)
        serializer = CommunicationSerializer(received_messages, many=True)
        return Response(serializer.data)

class SentMessageList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        sent_messages = Communication.objects.filter(sender_id=request.user.id)
        serializer = CommunicationSerializer(sent_messages, many=True)
        return Response(serializer.data)

class MessageDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Communication.objects.get(pk=pk)
        except Communication.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        message = self.get_object(pk)
        serializer = CommunicationSerializer(message)
        return Response(serializer.data)

    def delete(self, request, pk):
        message = self.get_object(pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)