#-*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.db import connection
from bbk.settings import SESSION_COOKIE_AGE
import pdb, traceback
import logging
from django.conf import settings #读取setting配置


logger = logging.getLogger(__name__)

DEBUG_PDB =settings.DEBUG_PDB

class BlockedIpMiddlewareMixin(MiddlewareMixin):
    """ip黑名單 """
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in getattr(settings, "BLOCKED_IPS", [] ):
            return django.http.HttpResponseForbidden('<h1>Forbiddent</h1>')


class CountOnlineMiddlewareMixin(MiddlewareMixin):


    def delete(self,cache_key ):
        if DEBUG_PDB:
            pdb.set_trace()
            from django.db import connection, transaction
            cursor = connection.cursor()

            #import datetime
            #datatime.datetime.strptime(datetime.now(), '%Y-%m-%d %H:%I:%S')
            # Data modifying operation - commit required
            cursor.execute("UPDATE my_cache_table SET expires =%s", [SESSION_COOKIE_AGE])
            transaction.commit_unless_managed()


    def update(self):
        if DEBUG_PDB:
            pdb.set_trace()
        from django.db import connection, transaction
        cursor = connection.cursor()

        #import datetime
        #datatime.datetime.strptime(datetime.now(), '%Y-%m-%d %H:%I:%S')
        # Data modifying operation - commit required
        cursor.execute("UPDATE my_cache_table SET expires =%s", [SESSION_COOKIE_AGE])
        transaction.commit_unless_managed()


    def getCount(self):
        if DEBUG_PDB:
            pdb.set_trace()
        from django.db import connection, transaction
        cursor = connection.cursor()

        # Data modifying operation - commit required
        #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        #transaction.commit_unless_managed()
        #Data retrieval operation - no commit required
        cursor.execute("SELECT count(distinct cache_key) FROM my_cache_table" )
        #return a tuple
        row = cursor.fetchone()[0]
        return row

    def process_request(self, request):
        logger.debug("process_request")
        if DEBUG_PDB:
	    pdb.set_trace()
        # 获取当前session key
        session_key = request.session.session_key
        # 获取当前访问用户的IP
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        # 判断用户是否登录
        if request.user.is_authenticated():
            # 因为已经在session中配置了自动更新时间了，下面操作不需要
            # # 在线的话每当用户访问页面要更新session 时间，防止session失效
            # request.session.set_expiry(SESSION_COOKIE_AGE)
            # 统计在线用户，先生成唯一key
            #online_key = 'count_online_id_{_id}_session_{_session}'.format(
            #_id=request.session.get('user_info')['id'], _session=session_key)
            # 设置过期时间，或者重新设置过期时间
            #cache.set(online_key, 'online', timeout=SESSION_COOKIE_AGE)
            pass
        else:
            pass

        # 把统计数放入请求中，方便在模板中使用
        # 通过通配符获取 count_online 的key 有多少个
        # 如果用户不再看网页，session 和 cache 的key 会自动过期，自动删除
        #request.online_member_count = len(cache.keys("count_online_id_*"))
        count = self.getCount()
        request.online_member_count = int(count)
        request.current_visitor_ip = ip

    # 用来查看sql语句的debug 关闭
    def process_response(self, request, response):
        logger.debug("process_view")
        #for query in connection.queries:
        #    nice_sql = query['sql'].replace('"', '').replace(',', ', ')
        #    sql = "\033[1;31m[%s]\033[0m %s" % (query['time'], nice_sql)
        #    print(sql)

        return response

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        logger.debug("process_view")
        pass

    def process_template_response(self,request,response):
        logger.debug("process_template_response")
        return response

    def process_exception(self, request, exception):
        logger.debug("process_exception")
        pass
