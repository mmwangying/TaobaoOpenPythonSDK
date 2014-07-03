#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 查询已采购的集分宝余额，操作流程如下： 1、申请支付宝增值包。 2、申请支付宝应用上线时选择集分宝API。 3、引导商家签约支付宝集分宝服务，地址为https://openapi.alipay.com/subscribe.htm?id=应用ID。 4、引导商家对授予支付宝集分宝发放权限，地址为https://openauth.alipay.com/oauth2/authorize.htm?scope=p&client_id=应用ID 5、引导授权的商家采购集分宝，地址为https://jf.alipay.com/aop/purchase.htm，进行集分宝采购。 6、商家采购之后可以通过集分宝余额API（alipay.point.budget.get）查询商家的集分宝数量。
# @author wuliang@maimiaotech.com
# @version: 0.0.0

import os
import sys
import time



def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

__modulePath = os.path.join(__getCurrentPath(), os.path.pardir)
__modulePath = os.path.normpath(__modulePath)
if __modulePath not in sys.path:
    sys.path.insert(0, __modulePath)


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">查询已采购的集分宝余额，操作流程如下： 1、申请支付宝增值包。 2、申请支付宝应用上线时选择集分宝API。 3、引导商家签约支付宝集分宝服务，地址为https://openapi.alipay.com/subscribe.htm?id=应用ID。 4、引导商家对授予支付宝集分宝发放权限，地址为https://openauth.alipay.com/oauth2/authorize.htm?scope=p&client_id=应用ID 5、引导授权的商家采购集分宝，地址为https://jf.alipay.com/aop/purchase.htm，进行集分宝采购。 6、商家采购之后可以通过集分宝余额API（alipay.point.budget.get）查询商家的集分宝数量。</SPAN>
# <UL>
# </UL>
class LipayPointBudgetGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "alipay.point.budget.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">支付宝给用户的授权。如果没有top的授权，这个字段是必填项</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">special</SPAN>
        # </LI>
        # </UL>
        self.auth_token = None
