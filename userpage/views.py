from codex.baseerror import *
from codex.baseview import APIView

from wechat.models import User, Activity, Ticket

import urllib.request
import urllib.parse
import http.cookiejar
import os

import time


class UserBind(APIView):
    def validate_user(self):
        """
        input: self.input['student_id'] and self.input['password']
        raise: ValidateError when validating failed
        """
        username = self.input['student_id']
        password = self.input['password']
        logurl = "https://info.tsinghua.edu.cn/Login"
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        params = {"userName": username, "password": password}
        params = urllib.parse.urlencode(params)
        params = params.encode('utf-8')
        response = urllib.request.urlopen(logurl, params)
        f = open("./return.html", "wb")
        f.write(response.read())

        target = "/render.userLayoutRootNode.uP"
        target1 = "/minichan/roamaction.jsp?id=149"
        flag = 0
        # 解决编码问题
        try:
            f = open("./return.html")

            for row in f.readlines():
                if (target in row) or (target1 in row):
                    print("got it")
                    flag = 1
                    break
            f.close()
        except:
            f = open("./return.html", "r", encoding="utf-8")
            for row in f.readlines():
                if (target in row) or (target1 in row):
                    print("got it")
                    flag = 1
                    break
            f.close()

        filename = "./return.html"
        if os.path.exists(filename):
            os.remove(filename)
        if flag == 1:
            return "successful validation"
        else:
            raise ValidateError("validation error")
            # raise NotImplementedError('You should implement UserBind.validate_user method')

    def get(self):
        self.check_input('openid')
        return User.get_by_openid(self.input['openid']).student_id

    def post(self):
        self.check_input('openid', 'student_id', 'password')
        user = User.get_by_openid(self.input['openid'])
        self.validate_user()
        user.student_id = self.input['student_id']
        user.save()


class ActivityDetail(APIView):
    def get(self):
        activity = Activity.objects.get(id=self.input['id'])
        if activity.status == Activity.STATUS_PUBLISHED:
            data = {
                'name': activity.name,
                'key': activity.key,
                'description': str(activity.description),
                'startTime': time.mktime(activity.start_time.timetuple()),
                'endTime': time.mktime(activity.end_time.timetuple()),
                'place': activity.place,
                'bookStart': time.mktime(activity.book_start.timetuple()),
                'bookEnd': time.mktime(activity.book_end.timetuple()),
                'totalTickets': activity.total_tickets,
                'picUrl': activity.pic_url,
                'remainTickets': activity.remain_tickets,
                'currentTime': time.mktime(time.localtime(time.time()))
            }
            return data
        else:
            raise ActivityDetailError("acticity not published yet")


class TicketDetail(APIView):
    def get(self):
        self.check_input('openid', 'ticket')
        myTicket = Ticket.get_by_uniqueId(self.input['ticket'])
        data = {
            'activityName': myTicket.activity.name,
            'place': myTicket.activity.place,
            'activityKey': myTicket.activity.key,
            'uniqueId': myTicket.unique_id,
            'startTime': time.mktime(myTicket.activity.start_time.timetuple()),
            'endTime': time.mktime(myTicket.activity.end_time.timetuple()),
            'currentTime': time.mktime(time.localtime(time.time())),
            'status': myTicket.status
        }
        return data
