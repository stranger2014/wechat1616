from django.contrib.auth import authenticate, login, logout

from codex.baseerror import *
from codex.baseview import APIView
from wechat.models import Activity
import time
from itertools import chain
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.

class AdminLogin(APIView):
    def get(self):
        if self.request.user.is_authenticated():
            return
        else:
            raise LoginError("Not login in")

    def post(self):
        self.check_input('username', 'password')
        username = self.input['username']
        password = self.input['password']
        try:
            user = authenticate(username=username, password=password)
        except:
            raise ValidateError("User not exit")
        try:
            login(self.request, user)
        except:
            raise LoginError("Can't login in")
        #f = open('1.txt', 'w')
        #f.write(username)
        #f.close()


class AdminLogout(APIView):

    def post(self):
        try:
            logout(self.request)
        except:
            raise LogoutError("Logout error")

class ActivityList(APIView):

    def get(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")
        try:
            activityList = chain(Activity.objects.filter(status = 0),Activity.objects.filter(status = 1))
            data = []
            for activity in activityList:
                acty = {'id': activity.id,
                        'name': activity.name,
                        'description': str(activity.description),
                        'startTime': time.mktime(activity.start_time.timetuple()),
                        'endTime': time.mktime(activity.end_time.timetuple()),
                        'place':  activity.place,
                        'bookStart': time.mktime(activity.book_start.timetuple()),
                        'bookEnd': time.mktime(activity.book_end.timetuple()),
                        'currentTime': time.localtime(time.time()),
                        'status': activity.status
                }
                data.append(acty)
            return data
        except:
            raise ActivityListError("获取活动列表失败")

class ActivityDelete(APIView):

    def post(self):
        self.check_input('id')
        try:
            Activity.objects.get(id = self.input['id']).delete()
        except:
            raise ActivityDeleteError("Delete error")

class ActivityCreate(APIView):

    def post(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")

        try:
            acty = Activity.objects.create(name = self.input['name'], key = self.input['key'], place = self.input['place'], description = self.input['description'],
                                    pic_url = self.input['picUrl'], start_time = self.input['startTime'], end_time = self.input['endTime'],
                                    book_start = self.input['bookStart'], book_end = self.input['bookEnd'], total_tickets = int(self.input['totalTickets']),
                                    status = int(self.input['status']), remain_tickets = int(self.input['totalTickets']))
            return acty.id
        except:
            raise ActivityCreateError("Create error")

class imageUpload(APIView):

    def post(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")

        self.check_input('image')
        image=self.request.FILES['image']

        #f = open('1.txt', 'w')
        #for i in image:
        #    f.write(i)
        #f.close()

        try:
            destination = open("D:\\1.jpg", 'wb+')
            for chunk in image:
                destination.write(chunk)
            destination.close()
            str="D:\\1.jpg"
            return str
        except:
            raise ImageUploadError("image upload error")

class ActivityDetail(APIView):

    def get(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")

        activity = Activity.objects.get(id = self.input['id'])
        data = {'name': activity.name,
                'key': activity.key,
                'description': str(activity.description),
                'startTime': time.mktime(activity.start_time.timetuple()),
                'endTime': time.mktime(activity.end_time.timetuple()),
                'place': activity.place,
                'bookStart': time.mktime(activity.book_start.timetuple()),
                'bookEnd': time.mktime(activity.book_end.timetuple()),
                'totalTickets': activity.total_tickets,
                'picUrl': activity.pic_url,
                'bookedTickets': 0,
                'usedTickets': 0,
                'currentTime': time.mktime(time.localtime(time.time())),
                'status': activity.status
                }
        #f = open('1.txt', 'w')
        #f.write(str(activity.status))
        #f.close()
        return data

    def post(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")

        try:
            activity = Activity.objects.get(id = self.input['id'])
            if 'name' in self.input:
                activity.name = self.input['name']
            if 'place' in self.input:
                activity.place = self.input['place']
            if 'description' in self.input:
                activity.description = self.input['description']
            if 'picUrl' in self.input:
                activity.pic_url = self.input['picUrl']
            if 'startTime' in self.input:
                activity.start_time = self.input['startTime']
            if 'endTime' in self.input:
                activity.end_time = self.input['endTime']
            if 'bookStart' in self.input:
                activity.book_start = self.input['bookStart']
            if 'bookEnd' in self.input:
                activity.book_end = self.input['bookEnd']
            if 'totalTickets' in self.input:
                activity.total_tickets = int(self.input['totalTickets'])
            if 'status' in self.input:
                activity.status = int(self.input['status'])
            activity.save()
        except:
            raise ActivityDetailError("Acticity change error")

class ActivityMenu(APIView):

    def get(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")
        actyList = []
        num = 1
        activityList = Activity.objects.filter(status = 1)
        for activity in activityList:
            acty = {'id':activity.id,
                    'name':activity.name,
                    'menuIndex':num
            }
            num += 1
            actyList.append(acty)
        return actyList

    def post(self):
        if not self.request.user.is_authenticated():
            raise LoginError("Not login in")

        return

class ActivityCheckin(APIView):

    def post(self):
        if not self.request.user.is_authenticated():
            return LoginError("Not login in")
        self.check_input('actId', 'ticket', 'studentId')

        return





