#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:



## @brief 此接口用于ISV订阅增量消息。  只有开通了增量消息角色的ISV才能开通增量消息的服务  如果ISV已经开通了增量消息服务，重复开通会跟据传入的参数更新ISV的服务记录（如：订阅字段、有效期限等等）  传入的topics消息类型的数量和顺序要和传入的status消息状态所属的类型的数量和顺序要一致。传了某个消息类型的topic却传入他对应位置的status为""(空字符串)时表示订阅这个topic下的所有消息  每次订阅操作如果是更新旧有数据，那么会进行替换操作，即：会使用当前传入要更新的数据置换久的数据，而不会执行合并的操作。例如：以前订阅了trade的所有消息，这次更新的时候传入了topic为refund，status为RefundSuccess。那么此时用户不是既定阅了交易所有的消息又定了退款成功的消息，而是只订阅了退款成功的消息。
# @author wuliang@maimiaotech.com
# @version: 0.0.16

from datetime import datetime
import os
import sys
import time

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)


    
from Domain.SubscribeMessage import SubscribeMessage



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 此接口用于ISV订阅增量消息。  只有开通了增量消息角色的ISV才能开通增量消息的服务  如果ISV已经开通了增量消息服务，重复开通会跟据传入的参数更新ISV的服务记录（如：订阅字段、有效期限等等）  传入的topics消息类型的数量和顺序要和传入的status消息状态所属的类型的数量和顺序要一致。传了某个消息类型的topic却传入他对应位置的status为""(空字符串)时表示订阅这个topic下的所有消息  每次订阅操作如果是更新旧有数据，那么会进行替换操作，即：会使用当前传入要更新的数据置换久的数据，而不会执行合并的操作。例如：以前订阅了trade的所有消息，这次更新的时候传入了topic为refund，status为RefundSuccess。那么此时用户不是既定阅了交易所有的消息又定了退款成功的消息，而是只订阅了退款成功的消息。</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">CName</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">ISV订阅增量消息</SPAN>
# </LI>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">不需用户授权</SPAN>
# </LI>
# </UL>
class IncrementAppSubscribeResponse(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()
        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的返回信息,包含状态等</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">dict</SPAN>
        # </LI>
        # </UL>
        self.responseStatus = None

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的响应内容</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>        
        self.responseBody = None

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">ISV的订购信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">SubscribeMessage</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # </UL>
        self.subscribe_message = None
        ''' 
        @ivar subscribe_message: ISV的订购信息; B{Level}: C{Object}; B{Required}: C{true}; B{Sample}: C{};
        @type subscribe_message: SubscribeMessage
        '''
    
        self.__init(kargs)
    
    def _newInstance(self, name, value):
        types = self._getPropertyType(name)
        propertyType = types[0]
        isArray = types[1]
        if propertyType == bool:
            if isArray:
                return [x for x in value[value.keys()[0]]]
            else:
                return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            if isArray:
                return [datetime.strptime(x, format) for x in value[value.keys()[0]]]
            else:
                return datetime.strptime(value, format)
        elif propertyType == str:
            if isArray:
                return [x.encode("utf-8") for x in value[value.keys()[0]]]
            else:
                return value.encode("utf-8")
        else:
            if isArray:
                return [propertyType(x) for x in value[value.keys()[0]]]
            else:
                return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "subscribe_message": "SubscribeMessage",
        }
        levels = {
            
            "subscribe_message": "Object",
        }
        
        nameType = properties[name]
        pythonType = None
        if nameType == "Number":
            pythonType = int
        elif nameType == "String":
            pythonType = str
        elif nameType == 'Boolean':
            pythonType = bool
        elif nameType == "Date":
            pythonType = datetime
        elif nameType == 'Field List':
            pythonType == str
        elif nameType == 'Price':
            pythonType = float
        elif nameType == 'byte[]':
            pythonType = str
        else:
            pythonType = getattr(sys.modules["Domain.%s" % nameType], nameType)
        
        # 是单个元素还是一个对象
        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)

    def __init(self, kargs):
        
        if kargs.has_key("subscribe_message"):
            self.subscribe_message = self._newInstance("subscribe_message", kargs["subscribe_message"])
        pass
